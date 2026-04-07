from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

R, C = map(int, input().split())
maze = [list(input()) for _ in range(R)]

f_dist = [[-1] * C for _ in range(R)]
j_dist = [[-1] * C for _ in range(R)]


f_queue = deque()
j_queue = deque()

for i in range(R):
    for j in range(C):
        if maze[i][j] == 'J':
            j_queue.append((i, j))
            maze[i][j] = '.'
            j_dist[i][j] = 0
        elif maze[i][j] == 'F':
            f_queue.append((i, j))
            f_dist[i][j] = 0

# 불 확산 시간 측정
while f_queue:
    x, y = f_queue.popleft()
        
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
    
        if 0 <= nx < R and 0 <= ny < C:
            # 이동할 수 있는 지역이고 아직 방문 안했는지 확인
            if maze[nx][ny] == '.' and f_dist[nx][ny] == -1:
                f_dist[nx][ny] = f_dist[x][y] + 1
                f_queue.append((nx, ny))
                    
# 지훈이의 이동 시간 측정
while(j_queue):
    x, y = j_queue.popleft()
        
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        # 범위 밖을 넘어가면 탈출
        if not (0 <= nx < R and 0 <= ny < C):
            print(j_dist[x][y] + 1)
            exit(0)
            
        if 0 <= nx < R and 0 <= ny < C:
            # 이동할 수 있는 지역이고 아직 방문 안했는지 확인
            if (maze[nx][ny] == '.' and j_dist[nx][ny] == -1
                # 불이 도달하지 못했거나 불이 퍼지는 속도보다 빠르게 이동한경우
                and (f_dist[nx][ny] == -1 or j_dist[x][y] + 1 < f_dist[nx][ny])):
                    j_dist[nx][ny] = j_dist[x][y] + 1
                    j_queue.append((nx, ny))
                    
print("IMPOSSIBLE")