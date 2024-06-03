'''
S->i + i->B + i->A
플로이드 워샬: 한점에서 다른 한 점까지 거리 계산
'''
def solution(n, s, a, b, fares):
    INF = 10000000
    answer = INF
    
    graph = [[INF] * (n+1) for _ in range(n+1)] # 전부 무한으로 초기화
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i == j:
                graph[i][j] = 0
    
    for f in fares:
        start, end, fare = f
        graph[start][end] = fare
        graph[end][start] = fare
        
    # 플로이드 워샬 수행
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
            
    for i in range(1, n+1):
        fare = graph[s][i] + graph[i][a] + graph[i][b]
        answer = min(answer, fare)
        
    return answer