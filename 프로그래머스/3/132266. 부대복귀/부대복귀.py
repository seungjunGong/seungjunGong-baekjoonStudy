from collections import deque

def solution(n, roads, sources, destination):
    graph = [[] for _ in range(n + 1)]

    # 무방향 그래프 만들기
    for a, b in roads:
        graph[a].append(b)
        graph[b].append(a)

    # destination에서 BFS 시작
    distance = [-1] * (n + 1)
    distance[destination] = 0

    queue = deque([destination])

    while queue:
        current = queue.popleft()

        for next_node in graph[current]:
            if distance[next_node] == -1:
                distance[next_node] = distance[current] + 1
                queue.append(next_node)

    # sources 순서대로 거리 반환
    return [distance[source] for source in sources]