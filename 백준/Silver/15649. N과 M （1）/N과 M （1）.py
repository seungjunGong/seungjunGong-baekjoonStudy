N, M = map(int,  input().split())
s = [0 for _ in range(N+1)]

visited = [0 for _ in range(N+1)]
def solution(k):
    # M 개 수열 만족
    if k == M:
        for i in range(M):
            print(s[i], end=" ")
        print()
        return
    # 수열 탐색
    for i in range(1, N+1):
        if visited[i]:
            continue
        visited[i] = True # 방문
        s[k] = i
        solution(k + 1)
        visited[i] = False # 회귀

solution(0)