def solution(n):
    answer = 0
    x = 2
    while x <= n:
        if n % x == 1:
            break
        x += 1
    answer = x
    return answer