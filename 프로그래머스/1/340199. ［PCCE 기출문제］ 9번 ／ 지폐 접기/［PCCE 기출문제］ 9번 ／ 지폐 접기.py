def max_min(le):
    if le[0] > le[1]: return le[0], le[1]
    else: return le[1], le[0]

def solution(wallet, bill):
    answer = 0

    w_max, w_min = max_min(wallet)
    b_max, b_min = max_min(bill)
    
    while(b_min > w_min or b_max > w_max):
        b_max //= 2
        b_max, b_min = max_min([b_max, b_min])
        answer += 1
    
    return answer