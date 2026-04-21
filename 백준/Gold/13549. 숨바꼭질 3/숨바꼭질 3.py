from collections import deque

N, K = map(int, input().split())

VISITED_SIZE = 2 * K + 1
visited = [-1 for _ in range(VISITED_SIZE)]
def find_brother():
    queue = deque()
    queue.append(N)
    visited[N] = 0 
    
    while(queue):
        x = queue.popleft()
        
        if x == K:
            print(visited[x])
            return
        
        move = [2 * x, x + 1, x - 1]
        for i, nx in enumerate(move):
            if 0 <= nx < VISITED_SIZE:
                # 0초인 경우
                if i == 0 and (visited[nx] == -1 or visited[nx] > visited[x]):
                    visited[nx] = visited[x]
                    queue.appendleft(nx) # 우선 탐색
                elif visited[nx] == -1:
                    visited[nx] = visited[x] + 1
                    queue.append(nx)

if N >= K:
    time = N - K
    print(time)
else:
    find_brother()