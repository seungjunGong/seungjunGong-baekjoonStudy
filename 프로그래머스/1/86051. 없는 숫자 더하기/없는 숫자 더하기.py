def solution(numbers):
    counts = [0 for _ in range(10)]
    
    for i in numbers:
        counts[i] = 1
    
    answer = sum([i for i in range(10) if counts[i] == 0])
    
    return answer