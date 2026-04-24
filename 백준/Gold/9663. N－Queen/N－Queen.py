N = int(input())

visited1 = [False for _ in range(N)]
visited2 = [False for _ in range(2*N-1)]
visited3 = [False for _ in range(2*N-1)]

cnt = 0
def solution(row):
    global cnt
    if row == N:
        cnt += 1
        return
    for col in range(N):
        if visited1[col] or visited2[col+row] or visited3[row-col+N-1]:
            continue
        visited1[col] = True # 열 방문
        visited2[col+row] = True # 왼쪽 대각선 방문
        visited3[row-col+N-1] = True # 오른쪽 대각선 방문
        
        solution(row+1) # 다음행 방문
        # 방문 초기화
        visited1[col] = False
        visited2[col+row] = False
        visited3[row-col+N-1] = False
        
solution(0)
print(cnt)