'''
양방향 리스트 그래프로 입력 받기
1. 연결 부 끊기
2. 각 연결된 부분끼리 카운트
3. 비교
'''
from collections import deque 

def bfs(graph, v, visited): # 연결리스트 bfs 구현

    queue = deque([v])
    
    visited[v] = True # 방문노드 처리
    cnt = 1

    while(queue):
        v = queue.popleft()
        
        for i in graph[v]:  # 방문하지 않는 원소 큐 삽입
            if not visited[i]:
                cnt += 1
                queue.append(i)
                visited[i] = True
    return cnt 

def solution(n, wires):
    answer = n - 2  # 두 전력망의 차이 최대값
    
    graph = [[] for _ in range(n+1)]    # 0~n 까지 리스트
    for start, end in wires:    # 인접리스트 그래프 생성
        graph[start].append(end)
        graph[end].append(start)
        
    for start, end in wires:
        visited = [False] * (n+1)
        visited[end] = True # 송전탑 끊기
        cnt = bfs(graph, start, visited)
        diff_cnt = abs(cnt - (n - cnt)) # 자르기전노드개수 - 자른 이후 노드 개수
        answer = min(answer, diff_cnt)
        
    return answer