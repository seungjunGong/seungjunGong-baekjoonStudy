def solution(t, p):
    answer = 0
    digit = len(p)
    p = int(p)
    
    for i in range(len(t)-digit+1):
        if int(t[i:i+digit]) <= p:
            answer += 1
    return answer