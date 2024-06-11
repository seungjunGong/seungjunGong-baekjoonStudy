'''
1번에서 n번까지 가는 가장 작은 거리 찾기
거리 계산 후 max 값으로 count
'''
from collections import deque

def bfs(graph, n, start):
    queue = deque([start])
    distance = [0, 0] + [n] * (n-1)
    
    mv = 0
    while queue:
        start = queue.popleft()
        
        for v in graph[start]:
            if graph[v] and distance[v] > distance[start]+1:
                distance[v] = distance[start] + 1
                mv = max(mv, distance[v]) 
                queue.append(v)
                
    return distance, mv

def solution(n, edge):
    answer = 0
    
    graph = [[] for _ in range(n+1)]
    for e in edge:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])
        
    distance, mv = bfs(graph,n,1)
    for d in distance:
        if d == mv:
            answer += 1
            
    return answer