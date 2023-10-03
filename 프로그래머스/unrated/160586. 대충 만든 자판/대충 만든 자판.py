def solution(keymap, targets):
    answer = []
    
    for target in targets:
        total_cnt = 0
        for t in target:
            cnt = 10000
            for keys in keymap:
                add = keys.find(t) + 1
                if add != 0:
                    cnt = min(cnt, add)
            total_cnt += cnt
        if total_cnt >= 10000:
            answer.append(-1)
        else:
            answer.append(total_cnt)
    return answer