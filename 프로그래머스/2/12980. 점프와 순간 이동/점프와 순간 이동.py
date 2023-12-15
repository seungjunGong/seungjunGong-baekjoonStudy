# 현재 상황에서 점프
# 현재 상황에서 순간이동
def solution(n):
    usage = 0
    
    while(n > 0):
        if n % 2 == 0:
            n //= 2
        else:
            n -= 1
            usage += 1
    
    
    return usage
        
        