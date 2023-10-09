def solution(s):
    answer = []
    s = list(s)
    s_index = {}
    
    for i, alp in enumerate(s):
        if s_index.get(alp) == None:
            answer.append(-1)
        else:
            answer.append(i - s_index[alp])
        s_index[alp] = i
                    
    return answer
