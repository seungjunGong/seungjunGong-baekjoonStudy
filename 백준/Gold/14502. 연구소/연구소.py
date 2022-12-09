'''
1. 3개의 벽이 존재할 수 있는 모든 경우의 수 찾기 
2. 이후 2를 찾으면 상하좌우로 1을 만날 때까지 2로 변환 1을 만나면 다시 상하좌우로 반복
3. 2과정이 종료되면 해당하는 graph의 0의 개수 카운트 
4. 카운트가 가장 큰 값을 출력
'''

n, m =  map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]
made_graph = [[0] * m for _ in range(n)] # 벽을 세운 뒤의 맵

result = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # 범위 내에 0인 값이 있으면 2로 변환
        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            if made_graph[nx][ny] == 0:
                made_graph[nx][ny] = 2
                virus(nx, ny) # 반복
# 벽이 3개 존재하면 종료
def dfs(cnt):
    global result
    if cnt == 3:
        for i in range(n):
            for j in range(m):
                made_graph[i][j] = graph[i][j] # 맵 복사
        # 바이러스 전파
        for i in range(n):
            for j in range(m):
                if made_graph[i][j] == 2:
                    virus(i, j)
        # 0의 개수 확인
        zero_cnt = 0
        for i in range(n):
            for j in range(m):
                if made_graph[i][j] == 0:
                    zero_cnt += 1
        result = max(result, zero_cnt)
        # 다시 새로운 경우 수행
        return        
    for i in range(n): 
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                dfs(cnt + 1)
                graph[i][j] = 0
          
dfs(0)
print(result)