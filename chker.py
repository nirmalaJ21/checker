import numpy as np

def build_board(size):
    board = np.random.choice(["Empty", "Red", "Black"], size=(size, size))
    return board

def get_count(board, item):
    return np.count_nonzero(board == item)
def resize_board(board, new_size):
    """
    Changes the size of a board.
    """
    return np.resize(board, new_size)


def pivot_board(board):
    """
    Pivots the board so that rows become columns and vice versa.
    """
    board_pivot = [[board[j][i] for j in range(len(board))] for i in range(len(board[0]))]

    # Print the pivot board in a tabular format
    for row in board_pivot:
        for elem in row:
            print(f"{elem:^6}", end='')
        print()

    return board_pivot

if __name__ == "__main__":
    print("This file is not intended to be run as a main.")
