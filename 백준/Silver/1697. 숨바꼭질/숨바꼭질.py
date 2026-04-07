from collections import deque

N, K = map(int, input().split())
MAX_SIZE = 100001
dist = [0 for _ in range(MAX_SIZE)]

queue = deque()
queue.append(N)

while queue:
    x = queue.popleft()
    
    # 동생을 찾은 경우, 가장 빠른 시간
    if x == K:
        print(dist[K])
        exit(0)
    
    for nx in (x - 1, x + 1, x * 2):
        if 0 <= nx < MAX_SIZE and dist[nx] == 0:
            dist[nx] = dist[x] + 1
            queue.append(nx)