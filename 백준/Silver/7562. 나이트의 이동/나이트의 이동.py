from collections import deque

dx = [2, 2, 1, -1, -2, -2, -1, 1]
dy = [-1, 1, 2, 2, 1, -1, -2, -2]

T = int(input())

def find_minimum_move_to_goal(dist, N, start, goal):
    a, b = start
    
    dist[a][b] = 0
    queue = deque()
    queue.append((a, b))

    while queue:
        x, y = queue.popleft()
        
        if (x, y) == goal:
            print(dist[x][y])
            return

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N:
                if dist[nx][ny] == -1:
                    queue.append((nx, ny))
                    dist[nx][ny] = dist[x][y] + 1
                    
for _ in range(T):
    N = int(input())
    
    dist = [[-1] * N for _ in range(N)]
    start = tuple(map(int, input().split()))
    goal = tuple(map(int, input().split()))

    find_minimum_move_to_goal(dist, N, start, goal)