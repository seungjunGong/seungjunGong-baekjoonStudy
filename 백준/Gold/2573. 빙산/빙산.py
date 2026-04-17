from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

N, M = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]
iceList = list()

for i in range(N):
    for j in range(M):
        if board[i][j] > 0:
            iceList.append((i, j, board[i][j])) # 현재 빙산의 위치, 높이

def calc(ice_idx):
    x, y, h = iceList[ice_idx]
    
    minus = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if board[nx][ny] == 0:
            minus += 1
            
    iceList[ice_idx] = (x, y, h - minus)

visited = list()
def bfs(a, b):
    queue = deque()
    queue.append((a, b))
    visited[a][b] = True
    
    while(queue):
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
        
            if 0 <= nx < N and 0 <= ny < M:
                if board[nx][ny] > 0 and not visited[nx][ny]:
                    queue.append((nx, ny))
                    visited[nx][ny] = True
        
def main():
    global visited
    global iceList
    year = 0
    
    while(iceList):
        # dfs(빙산의 수 파악)
        chunk = 0
        visited = [[False] * M for _ in range(N)] # 방문 상태 초기화
        for ice_idx in range(len(iceList)):
            x, y, h = iceList[ice_idx]

            # 방문자가 없을 경우
            if not visited[x][y]:
                chunk += 1

                # 덩어리가 2 이상일 경우
                if chunk > 1:
                    print(year)
                    return
                # 덩어리 찾기(방문 노드 확인)
                bfs(x, y)

        # 1년치 녹을 빙산 계산
        for ice_idx in range(len(iceList)):
            calc(ice_idx)

        newIceList = []
        for ice_idx in range(len(iceList)):
            x, y, h = iceList[ice_idx]

            if h <= 0:
                board[x][y] = 0
            else:
                board[x][y] = h
                newIceList.append((x, y, h))
        iceList = newIceList

        year += 1

    print(0)
    
main()