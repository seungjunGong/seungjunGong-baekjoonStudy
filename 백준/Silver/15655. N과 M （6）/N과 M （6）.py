N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))
s = [0 for _ in range(M)]

def solution(k, start):
    if k == M:
        print(" ".join(map(str, s)))
        return
    
    for i in range(start, N):
        s[k] = arr[i]
        solution(k+1, i+1)
solution(0, 0)