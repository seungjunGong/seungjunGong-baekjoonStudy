def solution(n, left, right):
    answer = []
    
    length = right - left + 1
    
    for _ in range(length):
        pos = (left//n, left%n)
        num = max(pos[0], pos[1]) + 1
        answer.append(num)
        left += 1
        
    return answer