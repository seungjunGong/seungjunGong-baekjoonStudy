A, B, C = map(int, input().split())

def solution(a, b, m):
    if b == 1:
        return a % m
    
    num = solution(a, b // 2, m)
    
    # 제곱 연산 수행
    num = num * num % m
    # 짝수(a^b = a^(b/2) * a^(b/2))
    if b % 2 == 0:
        return num
    # 홀수(a^b = a^(b/2) & a^(b/2 + 1))
    return num * a % m

print(solution(A, B, C))