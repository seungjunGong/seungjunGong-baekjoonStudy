def solution(e, starts):
    answer = []
    
    # 숫자 등장 횟수 구하기
    count = [0] * (e + 1)
    
    for i in range(1, e + 1):
        for j in range(i, e + 1, i):
            count[j] += 1
    
    # i 이상 e 이하에서 등장 횟수가 가장 많은 숫자
    best = [0] * (e + 1)
    best[e] = e
    
    for i in range(e - 1, 0, -1):
        if count[i] >= count[best[i+1]]:
            best[i] = i
        else:
            best[i] = best[i + 1]
            
    for start in starts:
        answer.append(best[start])
        
    return answer