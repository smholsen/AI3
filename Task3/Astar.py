# A* Using manhattan distance, not Euclidian. Because simpler :3


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
        self.isClosed = False

        self.backTracked = False

        # Previous Node
        self.previous_node = None

        # Is this node the goal node?
        self.isGoal = False

        # Tentative cost
        self.g = 0

        # Heuristic cost
        self.h = 0

        # Total (tent+heuristic)
        self.f = 0

        self.cost = 1

    def __str__(self):

        if self.backTracked:
            return '+'

        elif self.isClosed:
            return 'x'

        elif self.isVisited:
            return 'o'

        elif self.isGoal:
            return 'B'

        elif self.isStart:
            return 'A'

        elif self.isWall:
            return '#'
        elif self.isNormal:
            return '.'

    def assign_cost(self, character):
        if character == "w":
            self.cost = 100
        elif character == "m":
            self.cost = 50
        elif character == "f":
            self.cost = 10
        elif character == "g":
            self.cost = 5
        else:
            self.cost = 1


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

        # Y-axis
        for y in range(len(rows)):
            current_row = []
            # X-axis
            for x in range(len(rows[y])):
                # Skip newlines
                if rows[y][x] != '\n':
                    # Create a node with coordinates x, y
                    new_node = Node(self, y, x)

                    # Assign cost to the node
                    new_node.assign_cost(rows[y][x])

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

    def backtrack_from_goal(self):
        tmp = self.goal
        tmp.backTracked = True
        while tmp.previous_node:
            tmp = tmp.previous_node
            tmp.backTracked = True


class Astar:

    openList = []
    closedList = []

    # Sort the open list with regards to both current cost + heuristic
    def sort_open_list(self):
        self.openList = sorted(self.openList, key=lambda o: float(o.f))


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
        # While not completed: Run A* Algorithm and print board for every step.
        stop = False
        while len(game_map.algorithm.openList) != 0 and stop is not True:

            print()
            # If there are still nodes in the openList
            game_map.algorithm.sort_open_list()
            for a in game_map.algorithm.openList:
                print(str(a.f) + '||', end="")
            print()
            # time.sleep(0.1)  # delays for 5 seconds

            # Pick the best node
            current_node = game_map.algorithm.openList[0]
            for node in game_map.algorithm.openList:
                if node.f == current_node.f:
                    if node.h < current_node.h:
                        current_node = node
                else:
                    break

            game_map.algorithm.openList.pop(game_map.algorithm.openList.index(current_node))

            # Make node state visited.
            current_node.isVisited = True

            # Check which neighbour is best choice.
            neighbouring_nodes = game_map.get_neighbours(current_node)

            for nbr in neighbouring_nodes:
                if nbr not in game_map.algorithm.closedList:
                    # Check if visited node is goal node
                    if nbr.isGoal:
                        nbr.previous_node = current_node
                        stop = True
                        # Stop loop
                        break

                    # If it is a wall then skip it
                    if nbr.isWall:
                        continue

                    # if neighbour already exists
                    if nbr in game_map.algorithm.openList:
                        new_g = current_node.g + nbr.cost
                        print('NEW G:', new_g)
                        if new_g < nbr.g:
                            nbr.g = new_g
                            if not nbr.isStart:
                                nbr.previous_node = current_node
                        nbr.f = nbr.g + nbr.h
                    else:
                        nbr.g = current_node.g + nbr.cost
                        nbr.h = game_map.manhattan_distance(nbr)
                        if not nbr.isStart:
                            nbr.previous_node = current_node
                        nbr.f = nbr.g + nbr.h
                        game_map.algorithm.openList.append(nbr)

            game_map.algorithm.closedList.append(current_node)
            current_node.isClosed = True

            game_map.print_board()

        game_map.backtrack_from_goal()
        print('\n\n')
        game_map.print_board()


main()
