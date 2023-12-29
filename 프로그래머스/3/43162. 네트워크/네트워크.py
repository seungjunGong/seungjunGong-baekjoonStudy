# 인접 행렬 dfs
def dfs_mat(graph, v, visited):
    visited[v] = True
    for w in range(len(visited)): # 인접 정점 탐색
        if graph[v][w] and not visited[w]:
            dfs_mat(graph, w, visited)
            
def solution(n, computers):
    answer = 0
    
    visited = [False for _ in range(n)] # 방문 초기화
    
    for i in range(n):
        if visited[i] == False:
            answer += 1 # 네트워크 생성
            dfs_mat(computers, i, visited) # 네트워크 연결
            
    return answer