### REWRITE AIMED AT ACHIEVING GREATER EFFICIENCY
import numpy as np
list_board = ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#',
                '#', '#', '#', '#', '#', '#', '#', '#', '#', '#',
                '#', 'br', 'bn', 'bb', 'bq', 'bk', 'bb', 'bn', 'br', '#',
                '#', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp', '#',
                '#', '0', '0', '0', '0', '0', '0', '0', '0', '#',
                '#', '0', '0', '0', '0', '0', '0', '0', '0', '#',
                '#', '0', '0', '0', '0', '0', '0', '0', '0', '#',
                '#', '0', '0', '0', '0', '0', '0', '0', '0', '#',
                '#', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp', '#',
                '#', 'wr', 'wn', 'wb', 'wq', 'wk', 'wb', 'wn', 'wr', '#',
                '#', '#', '#', '#', '#', '#', '#', '#', '#', '#',
                '#', '#', '#', '#', '#', '#', '#', '#', '#', '#']

moves = {'N': [21, 19, 12, 8],
         'B' : [11, 9],
         'R': [10, 1],
         'Q' : [11, 10, 9, 1] }

class Board:
    def __init__(self, list_board):
        self.board = np.array(list_board)

    


