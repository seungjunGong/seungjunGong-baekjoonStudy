import sys
sys.setrecursionlimit(10**6) # 재귀 호출 제한 설정
n = int(sys.stdin.readline())

graph = [[] for _ in range(n+1)]
parents = [False] * (n + 1)

for _ in range(n-1):
    a, b = map(int, sys.stdin.readline().split())
    # 무방향 그래프 생성
    graph[a].append(b)
    graph[b].append(a)

def dfs(parent):
    # 트리의 자식 노드와 부모 노드 설정
    for node in graph[parent]:
        if not parents[node]: 
            parents[node] = parent
            dfs(node)

dfs(1)

for child in range(2, n+1):
    print(parents[child])