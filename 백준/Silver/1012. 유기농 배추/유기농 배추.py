from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

T = int(input())
board = list()
M, N, K = (0, 0, 0)

def bfs(a, b):
    queue = deque()
    
    queue.append((a, b))
    board[a][b] = 0
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < N and 0 <= ny < M:
                if board[nx][ny] == 1:
                    board[nx][ny] = 0
                    queue.append((nx, ny))

for _ in range(T):
    M, N, K = map(int, input().split())

    board = [[0] * M for _ in range(N)] # 가로 M 개 세로 N 개 리스트 생성

    for _ in range(K):
        x, y = map(int, input().split()) # 가로 x, 세로 y
        board[y][x] = 1

    count = 0
    for i in range(N):
        for j in range(M):
            if board[i][j] == 1:
                bfs(i, j)
                count += 1

    print(count)