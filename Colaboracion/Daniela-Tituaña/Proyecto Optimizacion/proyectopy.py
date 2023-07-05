def solve_n_queens(n):
    solutions = []
    board = [['.' for _ in range(n)] for _ in range(n)]
    solve_n_queens_util(n, 0, board, solutions)
    return solutions

def solve_n_queens_util(n, col, board, solutions):
    if col == n:
        solution = []
        for row in board:
            solution.append(''.join(row))
        solutions.append(solution)
        return

    for row in range(n):
        if is_safe(board, row, col):
            board[row][col] = 'Q'
            solve_n_queens_util(n, col + 1, board, solutions)
            board[row][col] = '.'

def is_safe(board, row, col):
    n = len(board)

    # Verificar si hay una reina en la misma columna
    for i in range(n):
        if board[i][col] == 'Q':
            return False

    # Verificar si hay una reina en la misma fila
    for j in range(col):
        if board[row][j] == 'Q':
            return False

    # Verificar si hay una reina en la misma diagonal hacia arriba
    i = row
    j = col
    while i >= 0 and j >= 0:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j -= 1

    # Verificar si hay una reina en la misma diagonal hacia abajo
    i = row
    j = col
    while i < n and j >= 0:
        if board[i][j] == 'Q':
            return False
        i += 1
        j -= 1

    return True

def print_board(board):
    for row in board:
        print(' '.join(row))
    print()

def plot_solution(board):
    n = len(board)

    for row in range(n):
        for col in range(n):
            if board[row][col] == 'Q':
                print('♛', end=' ')
            else:
                print('.', end=' ')
        print()
    print()

# Ejemplo de uso
n = 8
solutions = solve_n_queens(n)

for solution in solutions:
    plot_solution(solution)