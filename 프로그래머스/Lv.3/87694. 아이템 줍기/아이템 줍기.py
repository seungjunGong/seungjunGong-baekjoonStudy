from collections import deque

'''
idea1: 밖 부분, 사각형 테두리, 사각형 안에 따라 다른 값을 설정
       사각형 안이면 테두리를 그리지 않는다.
       
idea2: ㄷ 자와 같은 경우 bfs 시에 잘못된 경로로 이동할 수 있다.
       따라서 전체 배열의 크기와 사각형의 크기를 2배 키운다.
'''
def make_maps(rectangle):
    maps = [[-1 for _ in range(102)] for _ in range(102)]
    
    for r in rectangle:
        x1, y1, x2, y2 = map(lambda x: x*2, r) # 전체 좌표 2배
        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                if x1 < x < x2 and y1 < y < y2: # 테두리 안 채우기
                    maps[x][y] = 0
                elif maps[x][y] == -1: # 테두리 그리기
                    maps[x][y] = 1
    return maps
    
def bfs(graph, visited, v, target):
    x, y = v
    queue = deque([(x, y, 0)])
    visited[x][y] = True
    
    move_to = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    
    tx, ty = target
    while queue:
        x, y, move = queue.popleft()
        
        if x == tx and y == ty:
            return move // 2
        
        for i, j in move_to:
            nx, ny = x+i, y+j
            if graph[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny, move+1))
                
def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    
    v = (2*characterX, 2*characterY) # 시작 좌표 2배
    target = (2*itemX, 2*itemY)      # 목표 좌표 2배
    visited = [[False for _ in range(102)] for _ in range(102)]
    
    maps = make_maps(rectangle)
    answer = bfs(maps, visited, v, target)
    
    return answer