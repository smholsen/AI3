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



class AStar:
    def heuristic(a, b):
        (x1, y1) = a
        (x2, y2) = b
        return abs(x1 - x2) + abs(y1 - y2)

    def a_star_search(graph, start, goal):
        frontier = PriorityQueue()
        frontier.put(start, 0)
        came_from = {}
        cost_so_far = {}
        came_from[start] = None
        cost_so_far[start] = 0

        while not frontier.empty():
            current = frontier.get()

            if current == goal:
                break

            for next in graph.neighbors(current):
                new_cost = cost_so_far[current] + graph.cost(current, next)
                if next not in cost_so_far or new_cost < cost_so_far[next]:
                    cost_so_far[next] = new_cost
                    priority = new_cost + heuristic(goal, next)
                    frontier.put(next, priority)
                    came_from[next] = current

        return came_from, cost_so_far

print(BoardMap().board)