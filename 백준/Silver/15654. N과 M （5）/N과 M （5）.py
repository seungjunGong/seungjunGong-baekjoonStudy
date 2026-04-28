N, M = map(int, input().split())
arr = [0] + sorted(list(map(int, input().split())))
s = [0 for _ in range(M)]

visited = [False for _ in range(N+1)]
def solution(k):
    if k == M:
        print(" ".join(map(str, s)))
        return
    
    for i in range(1, N+1):
        if visited[i]:
            continue
        s[k] = arr[i]
        visited[i] = True
        solution(k+1)
        visited[i] = False
solution(0)        