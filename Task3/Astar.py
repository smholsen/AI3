
class Node:
    # Constructor

    def __init__(self, map, y, x, type):

        # Co-Ords
        self.x = x
        self.y = y

        # Need to tie the nodes to the current map object
        # self.map = map

        # Type of Node // Wall, Normal etc
        self.type = type

        # Previous Node
        self.previous_node = None

        # Score?


class Map:

    # 2d Array of board read from .txt file
    map = []

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

    def create_map(self, rows):

        # Y-axis
        for y in range(len(rows)):
            currentRow = []
            # X-axis
            for x in range(len(rows[y])):
                # Skip newlines
                if rows[y][x] != '\n':
                    # Create a node with coordinates x, y
                    newNode = Node(self, 'normal', y, x)




    # prints out the board line for line
    def print_board(self):
        for line in self.map:
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
    # Remove previous Map
    game_map.map = []

    tmp_read_map = []
    # Read map file
    f = open('../Maps/' + board_file, 'r')
    for line in f:
        tmp_read_map.append(line)

    game_map.create_map(tmp_read_map)

    # Create map object with mapToCompute





