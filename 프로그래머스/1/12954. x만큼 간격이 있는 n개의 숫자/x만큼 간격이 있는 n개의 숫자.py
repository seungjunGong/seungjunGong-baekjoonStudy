def solution(x, n):
    if x == 0:
        return [0 for _ in range(n)]
    answer = [i for i in range(x, x*(n+1), x)]
    return answer