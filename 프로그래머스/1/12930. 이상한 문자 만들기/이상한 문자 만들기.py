def solution(s):
    answer = ''
    
    i = -1
    for w in s:
        i += -(i+1) if w == ' ' else 1
        answer += w.upper() if i % 2 == 0 else w.lower()
    return answer