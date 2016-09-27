

class BoardMap:
    board = []

    # constructor:
    def __init__(self):
        return_map = []
        # Select map
        level = input("Enter board level (11, 12, 13, 14, 21, 22, 23 or 24)")
        board_file = BoardMap.options[level]
        # Read map file
        f = open('../Maps/' + board_file, 'r')
        for line in f:
            tmp = []
            for symbol in line:
                # lol
                if symbol != '\n':
                    tmp.append(symbol)
            return_map.append(tmp)

        self.board = return_map

    # prints out the board line for line
    def print_board(self):
        for line in self.board:
            print(line)

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
    # Constructor
    def __init__(self):

        # 2d Array of board read from .txt file
        self.map = []

        # Target to move to
        self.goal = None

        # Size of map
        self.max_x = None
        self.max_y = None



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


BoardMap().print_board()




