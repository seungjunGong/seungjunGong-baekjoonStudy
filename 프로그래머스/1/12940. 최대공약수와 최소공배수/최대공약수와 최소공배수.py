def gcd(n, m):
    if m == 0:
        return n
    return gcd(m, n % m)

def solution(n, m):
    answer = [gcd(n, m)]
    answer.append((n * m) // answer[0])
    return answer