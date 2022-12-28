'''
n개 행성 10만
3차원 좌표
비용은 abs(좌표끼리 뺀 값)의 가장 작은 값
n - 1 개 건설 모든 행성 연결시의 최소 비용 - 크루스칼
이중 반복문을 돌면서 입력 받은 데이터의 거리와 비용을 저장 한다.
각각의 행성에 번호를 부여해 노드를 만들고 이후 최소 비용을 구한다.
x 축 y 축 z 축을 기준으로 정렬을 수행한다음 n - 1개의 간선을 각각 고려하여 비교한다.
'''
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a) 
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n = int(input())
planets = []
parent = [0] * n

edges = []
result = 0

for i in range(n):
    parent[i] = i

x = []
y = []
z = []

for i in range(n):
    a, b, c = map(int, input().split())
    x.append((a, i))
    y.append((b, i))
    z.append((c, i))

x.sort()
y.sort()
z.sort()

for i in range(n - 1):
    edges.append((x[i + 1][0] - x[i][0], x[i][1], x[i + 1][1]))
    edges.append((y[i + 1][0] - y[i][0], y[i][1], y[i + 1][1]))
    edges.append((z[i + 1][0] - z[i][0], z[i][1], z[i + 1][1]))

edges.sort()

for edge in edges:
    cost, a, b = edge
    
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(result)