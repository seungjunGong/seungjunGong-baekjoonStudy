N, K = map(int, input().split())
time = [max(N, K) - min(N, K) for _ in range(100001)]

from collections import deque
def bfs():

    queue = deque([(N, 0)])    
    while(queue):
        v, res = queue.popleft()
        if 0 <= v <= 100000  and res < time[v]:
            time[v] = res
            queue.append((v+1, res+1))
            queue.append((v-1, res+1))
            queue.append((v*2, res+1))

bfs()
print(time[K])