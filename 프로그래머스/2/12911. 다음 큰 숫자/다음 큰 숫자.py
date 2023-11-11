def solution(n):
    answer = n
    
    while(1):
        answer += 1
        if format(n, 'b').count('1') == format(answer, 'b').count('1'):
            return answer
        
    return answer