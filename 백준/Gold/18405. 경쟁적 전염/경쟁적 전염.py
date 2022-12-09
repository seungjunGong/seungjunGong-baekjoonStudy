'''
입력 받은 값을 기준으로 상하좌우가 0이면 해당 바이러스 후순위로 추가 
상하좌우 전부 탐색 완료시 해당 바이러스 제거
나머지 반복
원하는 초일 경우 해당하는 값 출력
'''
from collections import deque

n, k = map(int, input().split())

graph = []
virus = []

for i in range(n):
    temp = list(map(int, input().split()))
    for j in range(n):
        if temp[j] != 0:
            virus.append((temp[j], 0, i, j)) # 바이러스 번호, 시간, x좌표, y좌표
    graph.append(temp)

virus.sort()
que = deque(virus)

target_s, target_x, target_y = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while que:
    virus_num, s, x, y = que.popleft()
    if target_s == s:
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and nx < n and ny >= 0 and ny < n:
            if graph[nx][ny] == 0:
                graph[nx][ny] = virus_num
                que.append((virus_num, s + 1, nx, ny)) # 시간과 함께 바이러스 위치 저장
    
print(graph[target_x - 1][target_y - 1])