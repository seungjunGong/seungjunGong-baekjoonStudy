def solution(k, m, score):
    answer = 0
    score.sort()
    
    for i in range(len(score)-m, -1, -m):
        answer += score[i] * m
        
    return answer