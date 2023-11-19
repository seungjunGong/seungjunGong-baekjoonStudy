def solution(absolutes, signs):
    answer = 123456789
    
    cal = (lambda sign, n : n if sign else n * (-1))
    answer = sum(cal(signs[i], absolutes[i]) for i in range(len(absolutes)))
    return answer