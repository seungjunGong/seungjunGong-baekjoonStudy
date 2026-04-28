N, M = map(int, input().split())
s = [0 for _ in range(M)]

def solution(k, start):
    if k == M:
        print(" ".join(map(str, s)))
        return 
    
    for i in range(start, N+1):
        s[k] = i
        solution(k+1, i)
solution(0, 1)