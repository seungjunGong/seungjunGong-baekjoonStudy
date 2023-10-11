def solution(k, score):
    answer = []
    honors = []
    
    for i, sc in enumerate(score):
        if i < k:
            honors.append(sc)
        else:
            min_honor = min(honors)
            if min_honor < sc:
                honors[honors.index(min_honor)] = sc
        answer.append(min(honors))
            
    return answer