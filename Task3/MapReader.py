class MapReader:

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

    @staticmethod
    def read():
        return_map = []
        # Select map
        board = input("Enter board level (11, 12, 13, 14, 21, 22, 23 or 24)")
        board_file = MapReader.options[board]
        # Read map file
        f = open('../Maps/' + board_file, 'r')
        for line in f:
            tmp = []
            for symbol in line:
                # lol
                if symbol != '\n':
                    tmp.append(symbol)
            return_map.append(tmp)

        return return_map



