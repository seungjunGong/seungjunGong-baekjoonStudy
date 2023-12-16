def solution(name, yearning, photo):
    answer = []
    
    for p in photo:
        score = 0
        for i in range(len(name)):
            score += p.count(name[i]) * yearning[i]
        answer.append(score)
        
    return answer