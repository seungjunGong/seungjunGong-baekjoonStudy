def solution(s):
    answer = 0
    
    same, diff = 1, 0
    i = 1
    first = s[0]
    while(i < len(s)-1):
        if first != s[i]:
            diff += 1
            if same == diff:
                answer += 1
                i += 1
                first = s[i]
                same, diff = 1, 0
        else:
            same += 1
        i += 1
                
    return answer + 1