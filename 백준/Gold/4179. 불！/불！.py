from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

R, C = map(int, input().split())
maze = [list(input()) for _ in range(R)]

f_dist = [[0] * C for _ in range(R)]
j_dist = [[0] * C for _ in range(R)]

def bfs():
    f_queue = deque()
    j_queue = deque()
    
    for i in range(R):
        for j in range(C):
            if maze[i][j] == 'J':
               j_queue.append((i, j))
               maze[i][j] = '.'
               j_dist[i][j] = 1
            elif maze[i][j] == 'F':
               f_queue.append((i, j))
               f_dist[i][j] = 1
    
    # 불 확산 시간 측정
    while(f_queue):
        x, y = f_queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < R and 0 <= ny < C:
                if maze[nx][ny] == '.' and f_dist[nx][ny] == 0:
                    f_dist[nx][ny] = f_dist[x][y] + 1
                    f_queue.append((nx, ny))
                    
    # 지훈이의 이동 시간 측정
    while(j_queue):
        x, y = j_queue.popleft()
        
        # 가장 자리시에 탈출
        if x == R - 1 or x == 0 or y == 0 or y == C - 1:
            print(j_dist[x][y])
            exit(0)
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < R and 0 <= ny < C:
                if (maze[nx][ny] == '.' 
                        and j_dist[nx][ny] == 0
                        and (f_dist[nx][ny] == 0 or j_dist[x][y] + 1 < f_dist[nx][ny])):
                    j_dist[nx][ny] = j_dist[x][y] + 1
                    j_queue.append((nx, ny))
                    
    print("IMPOSSIBLE")
        
bfs()