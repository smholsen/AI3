# A* Using manhattan distance, not Euclidian. Because simpler :3


class Node:
    # Constructor

    if __name__ == '__main__':
        def __init__(self, m_map, y, x, m_type):

            # Co-Ordinates
            self.x = x
            self.y = y

            # Need to tie the nodes to the current map object
            self.mMap = m_map

            # Type of Node // Wall, Normal etc
            self.mType = m_type

            # Previous Node
            self.previous_node = None

            # Is this node the goal node?
            self.goal = False

            # Tentative cost
            g = 0

            # Heuristic cost
            f = 0


class Map:

    # 2d Array of board read from .txt file
    mapArray = []

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

        algorithm = Astar()

        # Y-axis
        for y in range(len(rows)):
            current_row = []
            # X-axis
            for x in range(len(rows[y])):
                # Skip newlines
                if rows[y][x] != '\n':
                    # Create a node with coordinates x, y
                    new_node = Node(self, y, x, 'normal')

                    # If node is goal node, set Node.goal = true
                    if rows[y][x] == 'B':
                        new_node.goal = True
                        self.goal = new_node

                    # If node is start node, add node to A* Open set
                    if rows[y][x] == 'A':

                        algorithm.openList.append(new_node)

            # We need to set max width of map, but only once. I wasn't able to think of any better way to do it :p
            if self.max_x is None:
                self.max_x = len(current_row) - 1

        # Same with height
        if self.max_y is None:
            self.max_y = len(rows) - 1

        # If map was valid, we should now have 1 goal node and 1 start node.
        # Now we must set the tentative cost for start node. (g+f)
        if len(algorithm.openList) > 0:
            algorithm.openList[0].f = self.manhattan_distance(algorithm.openList[0])

    # Calculates the manhattan distance, adding difference in x and y between current node and goal node
    def manhattan_distance(self, from_node):
        return abs((self.goal.x - from_node.x) + abs(self.goal.y - from_node.y))

    # Prints out the board line for line
    def print_board(self):
        for line in self.mapArray:
            print(line)


class Astar:

    openList = []
    closedList = []
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
class Main:

    # Create Map Object
    game_map = Map()

    # Select map
    level = input("Enter board level (11, 12, 13, 14, 21, 22, 23 or 24)")
    board_file = Map.options[level]

    tmp_read_map = []
    # Read map file
    f = open('../Maps/' + board_file, 'r')
    for line in f:
        tmp_read_map.append(line)

    game_map.start_map(tmp_read_map)

    # Create map object with mapToCompute





