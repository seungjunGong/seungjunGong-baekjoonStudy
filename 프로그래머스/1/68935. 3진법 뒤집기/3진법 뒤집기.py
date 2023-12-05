def solution(n):
    answer = 0
    reverse = ""
    
    while n:
        reverse += str(n % 3)
        n //= 3
    
    d = 1
    for k in reverse[::-1]:
        answer += int(k) * d
        d *= 3
        
    return answer