def solution(d, budget):
    answer = 0
    d.sort()
    
    for expense in d:
        if budget < expense:
            break;
        budget -= expense
        answer += 1
        
    return answer