from collections import deque

dx = [0, 0 , 1, -1, 0, 0]
dy = [1, -1, 0, 0, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

M, N, H = map(int, input().split())

board = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H) ]
dist = [[[-1] * M for _ in range(N)] for _ in range(H) ]

queue = deque()
for a in range(H):
    for b in range(N):
        for c in range(M):
            if board[a][b][c] == 1:
                queue.append((a, b, c))
                dist[a][b][c] = 0
       
while queue:
    x, y, z = queue.popleft()
    
    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]
        nz = z + dz[i]
        
        if 0 <= nx < H and 0 <= ny < N and 0 <= nz < M:
            # 방문 안했는지 and 안익은 토마토인지
            if dist[nx][ny][nz] == -1 and board[nx][ny][nz] == 0:
                dist[nx][ny][nz] = dist[x][y][z] + 1
                queue.append((nx, ny, nz))

answer = 0
for a in range(H):
    for b in range(N):
        for c in range(M):
            # 안익은 토마토가 있는 경우
            if board[a][b][c] == 0 and dist[a][b][c] == -1:
                print(-1)
                exit(0)
            answer = max(dist[a][b][c], answer)
print(answer)