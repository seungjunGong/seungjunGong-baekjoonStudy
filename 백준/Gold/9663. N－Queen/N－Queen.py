ans = 0

def promising(row, colList):
    for i in range(row):
        if (colList[row] == colList[i]  # 열 체크
            or abs(colList[row] - colList[i]) == abs(row-i)):   # 대각선 체크
            return False
    return True

def n_queens(n, row, colList):
    global ans
    if row == n:
        ans += 1
        return
    
    for i in range(n):
        colList[row] = i
        if promising(row, colList):
            n_queens(n, row+1, colList)

n = int(input())
colList = [0] * n
n_queens(n, 0, colList)
print(ans)