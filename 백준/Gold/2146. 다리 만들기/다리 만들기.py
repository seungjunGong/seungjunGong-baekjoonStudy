from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
INF = 10001

N = int(input())
world = [list(map(int, input().split())) for _ in range(N)]

island_edges = dict()
island_id = 2
shortcut_dist = INF

def find_island(a, b):
    edges = []
    
    queue = deque()
    queue.append((a, b))
    world[a][b] = island_id
    
    while(queue):
        x, y = queue.popleft()
        
        is_edge = False
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < N and 0 <= ny < N:
                # 바다와 인접해 있으면 edge
                if world[nx][ny] == 0:
                    is_edge = True
                if world[nx][ny] == 1:
                    world[nx][ny] = island_id
                    queue.append((nx, ny))
        if is_edge:
            edges.append((x, y))
    
    island_edges[island_id] = edges

def find_shortcut(cur_id):
    queue = deque()
    visited = [[False] * N for _ in range(N)]
    
    for a, b in island_edges[cur_id]:
        queue.append((a, b, 0)) # 좌표, 현재 이동 거리
        visited[a][b] = True
        
    while(queue):
        x, y, dist = queue.popleft()
                
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < N and 0 <= ny < N:
                if not visited[nx][ny]:
                    # 바다인 경우
                    if world[nx][ny] == 0:
                        queue.append((nx, ny, dist + 1))
                        visited[nx][ny] = True
                     # 다른 섬을 만난경우
                    elif world[nx][ny] != cur_id:
                        return dist 
                    
    return INF                    

# 섬 찾기                    
for i in range(N):
    for j in range(N):
        if world[i][j] == 1:
            find_island(i, j)
            island_id += 1

# 최단 거리 구하기
for cur_id in island_edges:
    new_dist = find_shortcut(cur_id)
    shortcut_dist = min(shortcut_dist, new_dist)

print(shortcut_dist)