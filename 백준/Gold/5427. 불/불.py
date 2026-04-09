from collections import deque

dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]

T = int(input())

def find_exit_time(board, f_dist, s_dist, w, h):
    f_queue = deque()
    s_queue = deque()
    
    for i in range(h):
        for j in range(w):
            if board[i][j] == '*':
                f_queue.append((i, j))
                f_dist[i][j] = 0
            elif board[i][j] == '@':
                s_queue.append((i, j))
                s_dist[i][j] = 0
                
    # 불 퍼지는 시간 계산
    while f_queue:
        x, y = f_queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < h and 0 <= ny < w:
                if board[nx][ny] in ['.', '@'] and f_dist[nx][ny] == -1:
                    f_dist[nx][ny] = f_dist[x][y] + 1
                    f_queue.append((nx, ny))
                    
    # 상근이가 이동하는 시간 계산
    while s_queue:
        x, y = s_queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < h and 0 <= ny < w:
                # 빈 공간인지, 방문여부, 불이 퍼지는 속도보다 동시 혹은 먼저 이동 했는지 or 불이 오지 못하는 칸인지
                if (board[nx][ny] == '.' and s_dist[nx][ny] == -1
                    and (f_dist[nx][ny] > s_dist[x][y] + 1 or f_dist[nx][ny] == -1)):
                    s_dist[nx][ny] = s_dist[x][y] + 1
                    s_queue.append((nx, ny))
            else: # 범위를 벗어난 경우, 탈출
                print(s_dist[x][y] + 1)
                return True
    return False
    
for _ in range(T):
    w, h = map(int, input().split())
    
    board = [list(input()) for _ in range(h)]
    f_dist = [[-1] * w for _ in range(h)] # 불이 퍼지는 시간
    s_dist = [[-1] * w for _ in range(h)] # 상근이가 이동하는 시간
    
    if not find_exit_time(board, f_dist, s_dist, w, h):
        print("IMPOSSIBLE")