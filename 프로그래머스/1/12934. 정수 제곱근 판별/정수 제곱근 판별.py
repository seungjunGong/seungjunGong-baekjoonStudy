def solution(n):
    answer = int(n ** (0.5))
    if answer ** 2 == n:
        answer += 1
        answer = answer * answer
    else: answer = -1
    
    return answer