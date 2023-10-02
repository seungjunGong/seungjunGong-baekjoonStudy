def solution(n, m, section):
    answer = 0
    point = 0
    
    for p in section:
        if p >= point:
            point = p + m
            answer += 1
    return answer