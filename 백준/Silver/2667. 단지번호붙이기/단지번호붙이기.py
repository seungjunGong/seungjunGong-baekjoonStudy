N = int(input())

graph = [list(map(int, input())) for _ in range(N)]
move = [(0, 1), (1, 0), (-1, 0), (0, -1)]

def dfs(v):
    global cnt
    x, y = v
    if graph[x][y]:
        cnt += 1
        graph[x][y] = 0
        for i, j in move:
            mx, my = x + i, y + j
            if (mx > -1 and mx < N and my > -1 and my < N):
                dfs((mx, my))

res = []
global cnt
for i in range(N):
    for j in range(N):
        cnt = 0
        dfs((i, j))
        if cnt:
            res.append(cnt)
print(len(res))
for cnt in sorted(res):
    print(cnt)