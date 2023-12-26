def solution(citations):
    answer = len(citations)
    
    citations.sort(reverse=True)
    
    for i in range(len(citations)):
        if citations[i] <= i+1:
            answer = max(citations[i], i)
            break
            
    return answer