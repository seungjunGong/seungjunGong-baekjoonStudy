import math

def solution(n,a,b):
    answer = 0
    
    a, b = min(a, b), max(a, b)
    while(True):
        answer += 1
        
        if a + 1 == b and (a + b) % 4 == 3:
            break
        a, b = math.ceil(a/2), math.ceil(b/2)
        
    return answer