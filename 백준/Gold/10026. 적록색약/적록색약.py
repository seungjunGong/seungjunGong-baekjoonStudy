from collections import deque

N = int(input())

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
rg = ['R', 'G']

board = [list(input()) for _ in range(N)]
visited = [[''] * N for _ in range(N)]

def bfs(a, b, is_check_rg):
    queue = deque()
    
    visited[a][b] = board[a][b]
    queue.append((a, b))
    
    while queue:
        x, y = queue.popleft()
                
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < N and 0 <= ny < N:
                # 방문 했는지 확인
                if visited[nx][ny] == '':
                    if not is_check_rg: # 적록 색맹이면 G -> R
                        # 앞으로 이동할 위치(board) 와 현재 방문 위치(visited) 비교
                        if visited[x][y] in rg and board[nx][ny] in rg:
                            visited[nx][ny] = board[nx][ny]
                            queue.append((nx, ny))
                        elif visited[x][y] == board[nx][ny]:
                            visited[nx][ny] = board[nx][ny]
                            queue.append((nx, ny))
                    elif visited[x][y] == board[nx][ny]:
                        visited[nx][ny] = board[nx][ny]
                        queue.append((nx, ny))

# 적록 X
count = 0
for i in range(N):
    for j in range(N):
        if visited[i][j] == '':
            bfs(i, j, True)
            count += 1

# 적록 O
rb_count = 0
visited = [[''] * N for _ in range(N)] # 초기화
for i in range(N):
    for j in range(N):
        if visited[i][j] == '':
            bfs(i, j, False)
            rb_count += 1
print(count, rb_count)