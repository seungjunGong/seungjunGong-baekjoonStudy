from collections import deque
# 인접 행렬 dfs
def bfs_mat(graph, v, visited):
    
    visited[v] = True
    queue = deque([v])
    
    while(queue):
        v = queue.popleft()
        
        for w in range(len(visited)): # 인접 정점 탐색
            if graph[v][w] and not visited[w]:
                queue.append(w)
                visited[w] = True
            
def solution(n, computers):
    answer = 0
    
    visited = [False for _ in range(n)] # 방문 초기화
    
    for i in range(n):
        if visited[i] == False:
            answer += 1 # 네트워크 생성
            bfs_mat(computers, i, visited) # 네트워크 연결
            
    return answer