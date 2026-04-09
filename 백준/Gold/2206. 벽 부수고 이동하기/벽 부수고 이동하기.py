from collections import deque

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

N, M = map(int, input().split())
board = [list(map(int, input())) for _ in range(N)]
dist = [[[-1] * 2 for _ in range(M)] for _ in range(N)] 

queue = deque()
queue.append((0, 0, 0))
dist[0][0][0] = 1

while queue:
    x, y, broken = queue.popleft()
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        # 방문 여부 확인
        if 0 <= nx < N and 0 <= ny < M:
            # 지나갈 수 있는 공간인지, 방문여부 확인
            if board[nx][ny] == 0 and dist[nx][ny][broken] == -1:
                # 이전 상태 유지
                dist[nx][ny][broken] = dist[x][y][broken] + 1
                queue.append((nx, ny, broken))
            # 벽이 있는 경우, 부순후의 방문여부 확인
            elif board[nx][ny] == 1 and dist[nx][ny][1] == -1:
                # 벽 부술 수 있는지 확인
                if broken == 0:
                    dist[nx][ny][1] = dist[x][y][0] + 1
                    queue.append((nx, ny, 1))
                    
a = dist[N-1][M-1][0]
b = dist[N-1][M-1][1]                    
answer = [x for x in [a, b] if x != -1]
print(min(answer) if answer else -1)