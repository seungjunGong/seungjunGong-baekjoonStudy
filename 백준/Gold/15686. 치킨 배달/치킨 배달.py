'''
도시의 각 칸은 빈칸, 치킨집, 집 중 하나
도시의 칸은 (r, c) 형태 
치킨 거리 집을 기준으로 가장 가장 가까운 치킨집의 거리
'''
from itertools import combinations

n, m = map(int, input().split())
INF = 1e9

chicken = []
house = []

for a in range(n):
    array = list(map(int, input().split()))
    for b in range(n):
        if array[b] == 1:
            house.append((a, b))
        if array[b] == 2:
            chicken.append((a, b))

# 모든 치킨 집 중에서 m개의 치킨집을 뽑는 조합
combination = list(combinations(chicken, m))
result = INF

def get_sum(combination):
    result = 0
    for xh, yh in house:
        tmp = INF
        for xc, yc in combination:
            dist = abs(xh - xc) + abs(yh - yc)
            tmp = min(tmp, dist)
        result += tmp
    return result

for c in combination:
    result = min(result, get_sum(c))

print(result)