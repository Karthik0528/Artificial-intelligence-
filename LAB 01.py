n = 8
board = [["." for _ in range(n)] for _ in range(n)]

def print_board():
    for row in board:
        print(" ".join(row))
    print("\n")

def is_safe(row, col):
    for i in range(col):
        if board[row][i] == "X":
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == "X":
            return False
    for i, j in zip(range(row, n), range(col, -1, -1)):
        if board[i][j] == "X":
            return False
    return True

def solve():
    col = 0
    stack = []
    while True:
        if col == n:
            print_board()
            if not stack:
                break
            row, col = stack.pop()
            board[row][col] = "."
            col += 1
        else:
            placed = False
            for row in range(n):
                if is_safe(row, col):
                    board[row][col] = "X"
                    stack.append((row, col))
                    col += 1
                    placed = True
                    break
            if not placed:
                if not stack:
                    print("Solution does not exist")
                    break
                row, col = stack.pop()
                board[row][col] = "."
                col += 1

solve()

