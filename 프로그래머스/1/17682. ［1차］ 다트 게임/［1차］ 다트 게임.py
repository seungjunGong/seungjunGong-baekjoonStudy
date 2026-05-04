def solution(dartResult):
    scoreList = []
    
    idx = 0
    while idx < len(dartResult):
        if dartResult[idx:idx+2] == "10":
            res = 10
            idx += 1
        else:
            res = int(dartResult[idx])
        
        score = 0
        if dartResult[idx+1] == 'S':
            score = res
        elif dartResult[idx+1] == 'D':
            score = res ** 2
        elif dartResult[idx+1] == 'T':
            score = res ** 3
        
        if idx + 2 < len(dartResult):
            if dartResult[idx+2] == '*':
                score = score * 2
                if scoreList:
                    scoreList[-1] *= 2
                idx += 1
            elif dartResult[idx+2] == '#':
                score = (-1) * score
                idx += 1
        scoreList.append(score)
        idx += 2
        
    answer = sum(scoreList)
    return answer