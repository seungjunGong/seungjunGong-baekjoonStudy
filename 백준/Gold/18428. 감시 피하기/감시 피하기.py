'''
T 를 만나기 전까지 탐색 진행
S 를 만나면 만나기 전 인덱스의 값을 O로 변경 장애물 - 1
장애물이 0개가 될 때까지 or 현재 탐색하고자 하는 범위를 넘어설
때 까지 수행
'''
from itertools import combinations

n = int(input())

graph = []
teachers = []
empty = []

for i in range(n):
    graph.append(list(input().split()))
    for j in range(n):
        if graph[i][j] == 'T':
            teachers.append((i, j))
        if graph[i][j] == 'X':
            empty.append((i, j))
   
def dfs(x, y, direction):
    # 왼쪽
    if direction == 0:
        while y >= 0:
            if graph[x][y] == 'S':
                return True
            if graph[x][y] == 'O':
                return False
            y -= 1
    if direction == 1:
        while y < n:
            if graph[x][y] == 'S':
                return True
            if graph[x][y] == 'O':
                return False
            y += 1
    if direction == 2:
        while x >= 0:
            if graph[x][y] == 'S':
                return True
            if graph[x][y] == 'O':
                return False
            x -= 1
    if direction == 3:
        while x < n:
            if graph[x][y] == 'S':
                return True
            if graph[x][y] == 'O':
                return False
            x += 1
    return False

# 학생 발견 확인
def check_detect():
    for x, y in teachers:
        for i in range(4):
            if dfs(x, y, i):
                return True
    return False

result = False

# 비어있는 공간의 모든 경우에 장애물 설치
for index in combinations(empty, 3):
    for x, y in index:
        graph[x][y] = 'O'
    if not check_detect():
        result = True
        break
    for x, y in index:
        graph[x][y] = 'X'

print("YES" if result else "NO")