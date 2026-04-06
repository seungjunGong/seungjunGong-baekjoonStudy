from collections import deque

m, n = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

dist = [[0] * m for _ in range(n)]

def bfs():
    queue = deque()
    
    for i in range(n):
        for j in range(m):
            if box[i][j] == 1:
                queue.append((i, j))
                dist[i][j] = 1
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m:
                if box[nx][ny] == 0 and dist[nx][ny] == 0:
                    dist[nx][ny] = dist[x][y] + 1
                    box[nx][ny] = 1
                    queue.append((nx, ny))

bfs()

answer = 0

for i in range(n):
    for j in range(m):
        if box[i][j] == 0:  # 아직 안 익은 토마토
            print(-1)
            exit(0)
        answer = max(answer, dist[i][j])

print(answer - 1)