#!/usr/bin/python3
"""
NQueens
"""
import sys


def is_safe(board: list[int], row: int, col: int, n: int) -> bool:
    """
    Checks if the board is safe
    :param board:
    :param row:
    :param col:
    :param n:
    :return:
    """

    for i in range(row):
        if board[i] == col:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i] == j:
            return False

    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i] == j:
            return False

    return True


def solve_nqueens(board: list[int],
                  row: int, n: int) -> list[list[int]] | None:
    if row == n:
        solution = [[i, board[i]] for i in range(n)]
        print(solution)
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row] = col
            solve_nqueens(board, row + 1, n)
            board[row] = -1


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: nqueens N\n')
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if not isinstance(n, int):
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        exit(1)

    board: list[int] = [-1] * n

    print(solve_nqueens(board, 0, n))
