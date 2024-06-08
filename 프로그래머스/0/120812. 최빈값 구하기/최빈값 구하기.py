def solution(array):
    counts = [0 for _ in range(1000)]
    answer = [0, 0]
    
    for i in array:
        counts[i] += 1
        answer = [i, counts[i]] if answer[1] < counts[i] else answer
    
    counts.sort()
    answer = -1 if counts[-1] == counts[-2] else answer[0]
    
    return answer