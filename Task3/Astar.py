# A* Using manhattan distance, not Euclidian. Because simpler :3
import time


class Node:
    # Constructor

    def __init__(self, m_map, y, x):

        # Co-Ordinates
        self.x = x
        self.y = y

        # Need to tie the nodes to the current map object
        self.mMap = m_map

        self.isStart = False
        self.isWall = False
        self.isNormal = True
        self.isVisited = False

        # Previous Node
        self.previous_node = None

        # Is this node the goal node?
        self.isGoal = False

        # Tentative cost
        self.g = 0

        # Heuristic cost
        self.h = 0

    def __str__(self):

        if self.isVisited:
            return 'O'

        elif self.isGoal:
            return 'B'

        elif self.isStart:
            return 'A'

        elif self.isWall:
            return '#'

        elif self.isNormal:
            return '.'




class Map:

    # 2d Array of board read from .txt file
    mapArray = []
    algorithm = None

    # Constructor
    def __init__(self):

        # Target to move to
        self.goal = None

        # Size of map
        self.max_x = None
        self.max_y = None

    # Map options
    options = {
        '11': "board-1-1.txt",
        '12': "board-1-2.txt",
        '13': "board-1-3.txt",
        '14': "board-1-4.txt",
        '21': "board-2-1.txt",
        '22': "board-2-2.txt",
        '23': "board-2-3.txt",
        '24': "board-2-4.txt"
    }

    def start_map(self, rows):

        self.algorithm = Astar()
        # Reset map
        mapArray = []

        # Y-axis
        for y in range(len(rows)):
            current_row = []
            # X-axis
            for x in range(len(rows[y])):
                # Skip newlines
                if rows[y][x] != '\n':
                    # Create a node with coordinates x, y
                    new_node = Node(self, y, x)

                    # If node is goal node, set Node.goal = true
                    if rows[y][x] == 'B':
                        new_node.isGoal = True
                        self.goal = new_node

                    # If node is start node, add node to A* Open set
                    if rows[y][x] == 'A':
                        new_node.isStart = True
                        self.algorithm.openList.append(new_node)

                    elif rows[y][x] == '#':
                        new_node.isWall = True
                        # Walls are not possible to go to, so they are directly added to the A* closed set.
                        self.algorithm.closedList.append(new_node)

                    # If node is not start, end or wall then type = 'normal'
                    else:
                        new_node.mType = 'normal'

                    # Add node to row in map
                    current_row.append(new_node)

            # Add row to complete map.
            self.mapArray.append(current_row)

            # We need to set max width of map, but only once. I wasn't able to think of any better way to do it :p
            if self.max_x is None:
                self.max_x = len(current_row) - 1

        # Same with height
        if self.max_y is None:
            self.max_y = len(rows) - 1

        # If map was valid, we should now have 1 goal node and 1 start node.
        # Now we must set the tentative cost for start node. (g+f)
        if len(self.algorithm.openList) > 0:
            self.algorithm.openList[0].f = self.manhattan_distance(self.algorithm.openList[0])

    # Calculates the manhattan distance, adding difference in x and y between current node and goal node
    def manhattan_distance(self, from_node):
        return abs((self.goal.x - from_node.x) + abs(self.goal.y - from_node.y))

    # Get a list of neighbouring nodes of a given node
    def get_neighbours(self, node):
        # Init array for the parents
        neighbours = []

        # Check if node is located at edge of map, if not, add neighbour to list and return list.
        if node.y > 0:  # Up
            neighbours.append(self.mapArray[node.y - 1][node.x])
        if node.y < self.max_y:  # Down
            neighbours.append(self.mapArray[node.y + 1][node.x])
        if node.x > 0:  # Left
            neighbours.append(self.mapArray[node.y][node.x - 1])
        if node.x < self.max_x:  # Right
            neighbours.append(self.mapArray[node.y][node.x + 1])

        # Returns neighbours of the node
        return neighbours

    # Prints out the board line for line
    def print_board(self):
        for line in self.mapArray:
            for node in line:
                print(node, end="")
            print()



class Astar:

    openList = []
    closedList = []

    # Sort the open list with regards to both current cost + heuristic
    def sort_open_list(self):
        self.openList = sorted(self.openList, key=lambda total: total.g + total.h)

    #

    '''
    http://web.mit.edu/eranki/www/tutorials/search/
    // A *
    initialize the open list
    initialize the closed list
    put the starting node on the open list (you can leave its f at zero)

    while the open list is not empty
        find the node with the least f on the open list, call it "q"
        pop q off the open list
        generate q's 8 successors and set their parents to q
        for each successor
            if successor is the goal, stop the search
            successor.g = q.g + distance between successor and q
            successor.h = distance from goal to successor
            successor.f = successor.g + successor.h

            if a node with the same position as successor is in the OPEN list \
                which has a lower f than successor, skip this successor
            if a node with the same position as successor is in the CLOSED list \
                which has a lower f than successor, skip this successor
            otherwise, add the node to the open list
        end
        push q on the closed list
    end
    '''


# To run when start program
def main():

    # Create Map Object
    game_map = Map()

    # Select map
    level = input("Enter board level (11, 12, 13, 14, 21, 22, 23 or 24)")
    board_file = Map.options[level]

    algoType = input("What Algorithm to use? 0 = A*, 1 = BFS, 2 = Dijkstra")

    tmp_read_map = []
    # Read map file
    f = open('../Maps/' + board_file, 'r')
    for line in f:
        tmp_read_map.append(line)

    game_map.start_map(tmp_read_map)
    game_map.print_board()

    # If algorithm is set to A*
    if algoType == '0':
        current_node = None
        # While not completed: Run A* Algorithm and print board for every step.
        while True:
            print()
            time.sleep(0.5)  # delays for 5 seconds
            # If there are still nodes in the openList
            if len(game_map.algorithm.openList) != 0:
                game_map.algorithm.sort_open_list()

            # Pick the best node
            current_node = game_map.algorithm.openList[0]
            # Make node state visited.
            current_node.isVisited = True

            # Check if visited node is goal node


            game_map.print_board()
            break



main()



