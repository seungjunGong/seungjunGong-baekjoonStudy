def solution(n, s):
    answer = []
    
    
    if s < n:
        return [-1]
    
    num = s // n
    rest = s % n
    
    for _ in range(n):
        answer.append(num)
    
    if rest != 0:
        for i in range(n):
            answer[i] += 1
            rest -= 1
            if rest == 0:
                break
    
    answer.sort()
    return answer