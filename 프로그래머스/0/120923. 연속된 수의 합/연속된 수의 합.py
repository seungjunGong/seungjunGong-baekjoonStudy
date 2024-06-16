def solution(num, total):
    s = (total*2/num - num + 1 ) / 2    
    answer = [s+i for i in range(num)]
    return answer