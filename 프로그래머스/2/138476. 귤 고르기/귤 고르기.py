def solution(k, tangerine):
    answer = 0
    counts = {}
    
    for t in tangerine:
        counts[t] = counts.get(t, 0) + 1
        
    counts = sorted(counts.values(), reverse=True)
    
    for count in counts:
        answer += 1
        if k <= count:
            break
        k -= count
    
    return answer