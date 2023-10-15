def solution(ingredient):
    answer = 0
    hambuger = [1, 2, 3, 1]    
    check = 0
    
    while check < len(ingredient)-3:
        if ingredient[check:check+4] == hambuger:
            answer += 1
            del ingredient[check:check+4]
            check = check - 4 if check > 3 else -1
        check += 1
        
    return answer