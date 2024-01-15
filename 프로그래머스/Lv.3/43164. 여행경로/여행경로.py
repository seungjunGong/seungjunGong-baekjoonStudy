def dfs(graph, visited, v, route):
    
    global answer
    
    if len(route) == len(graph) + 1:
        answer = route
        return True
    
    for i in range(len(graph)):
        if v == graph[i][0] and not visited[i]:
            visited[i] = True
            if dfs(graph, visited, graph[i][1], route + [graph[i][1]]):
                return
            visited[i] = False

def solution(tickets):
    global answer
    answer = []
    visited = [False for _ in tickets]

    tickets.sort()
    dfs(tickets, visited, "ICN", ["ICN"])
    
    return answer