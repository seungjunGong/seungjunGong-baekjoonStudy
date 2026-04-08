from collections import deque

N = int(input())

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(a, b, board, visited):
    queue = deque()
    
    visited[a][b] = True
    queue.append((a, b))
    color = board[a][b] # 시작점 color
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < N and 0 <= ny < N:
                # 방문 했는지 확인 & 다음 위치 방문 가능 여부 확인
                if not visited[nx][ny] and color == board[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny))

board = [list(input()) for _ in range(N)]
rg_board = [[''] * N for _ in range(N)]

# 적록 색맹용 보드 전처리
for i in range(N):
    for j in range(N):
        if board[i][j] in ['R', 'G']:
            rg_board[i][j] = 'R'
        else:
            rg_board[i][j] = 'B'
            
rgb_visited = [[False] * N for _ in range(N)]
rg_visited = [[False] * N for _ in range(N)]

count = 0 # 적록 X
rg_count = 0 # 적록 O
for i in range(N):
    for j in range(N):
        if rgb_visited[i][j] == False:
            bfs(i, j, board, rgb_visited)
            count += 1
        if rg_visited[i][j] == False:
            bfs(i, j, rg_board, rg_visited)
            rg_count += 1

print(count, rg_count)