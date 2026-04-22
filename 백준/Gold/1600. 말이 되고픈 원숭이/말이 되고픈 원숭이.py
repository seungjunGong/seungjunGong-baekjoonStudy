from collections import deque

hx = [2, -2, 2, -2, 1, 1, -1, -1]
hy = [1, 1, -1, -1, 2, -2, 2, -2]
mx = [0, 0, 1, -1]
my = [1, -1, 0, 0]

K = int(input())
W, H = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(H)]
visited = [[[-1] * (K + 1) for _ in range(W)] for _ in range(H)]

queue = deque()
queue.append((0, 0, 0)) # x, y 좌표, 말 사용 횟수
visited[0][0][0] = 0

while(queue):
    x, y, hk = queue.popleft()
    
    if x == H - 1 and y == W - 1:
        print(visited[x][y][hk])
        exit(0)
    
    if hk < K:
        for i in range(8):
            nx = x + hx[i]
            ny = y + hy[i]
            nk = hk + 1
            
            if 0 <= nx < H and 0 <= ny < W:
                if board[nx][ny] == 0 and visited[nx][ny][nk] == -1:
                    visited[nx][ny][nk] = visited[x][y][hk] + 1
                    queue.append((nx, ny, nk))
    
    for i in range(4):
        nx = x + mx[i]
        ny = y + my[i]
        
        if 0 <= nx < H and 0 <= ny < W:
            if board[nx][ny] == 0 and visited[nx][ny][hk] == -1:
                visited[nx][ny][hk] = visited[x][y][hk] + 1
                queue.append((nx, ny, hk))
print(-1)