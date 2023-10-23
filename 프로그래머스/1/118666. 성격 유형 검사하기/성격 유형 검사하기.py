def solution(survey, choices):
    answer = ''
    type = {'R' : 0, 'T' : 0,
            'C' : 0, 'F' : 0,
            'J' : 0, 'M' : 0,
            'A' : 0, 'N' : 0}
    line = ["RT", "CF", "JM", "AN"]
    score = [0, 3, 2, 1, 0, 1, 2, 3]
    
    for i, s in enumerate(survey):
        if choices[i] > 4:
            type[s[1]] += score[choices[i]]
        else:
            type[s[0]] += score[choices[i]]
    
    print(type)
    for li in line:
        select = li[0] if type[li[0]] >= type[li[1]] else li[1]
        answer += select
    return answer