n = 4

board = [-1] * n

def safe(row, col):

    for i in range(row):

        if board[i] == col or abs(board[i] - col) == abs(i - row):
            return False

    return True


def solve(row):

    if row == n:
        print(board)
        return

    for col in range(n):

        if safe(row, col):

            board[row] = col

            solve(row + 1)

            board[row] = -1


solve(0)
