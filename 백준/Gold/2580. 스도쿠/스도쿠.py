N = 9
def promising(num, x, y, board):
    xb = (x // 3) * 3
    yb = (y // 3) * 3

    for i in range(N):      
        if board[i][y] == num:  # 열 체크
            return False
        if board[x][i] == num:  # 행 체크
            return False
        xi, yi = xb + i // 3, yb + i % 3
        if board[xi][yi] == num:   # 3x3 체크
            return False
    return True

def sudoku(board, blanks, bi):  # bi: blanks index 
    if bi == len(blanks):
        for b in board:
            print(*b)
        exit(0)
    
    x, y = blanks[bi]
    for i in range(1, N+1):
        if promising(i, x, y,board):
            board[x][y] = i
            sudoku(board, blanks, bi+1)
            board[x][y] = 0

board = [list(map(int, input().split())) for _ in range(N)]
blanks = [(i, j) for i in range(N) for j in range(N) if board[i][j] == 0]

sudoku(board, blanks, 0)