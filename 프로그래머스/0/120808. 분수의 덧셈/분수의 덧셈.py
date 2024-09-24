def solution(numer1, denom1, numer2, denom2):
    answer = [numer1*denom2 + numer2*denom1, denom1*denom2]
    
    i = 2
    while i < 1000000:
        if answer[0] % i == 0 and answer[1] % i == 0:
            answer[0] /= i
            answer[1] /= i
        else:
            i += 1
            
    return answer