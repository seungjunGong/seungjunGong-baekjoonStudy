def solution(numbers):
    answer = []
    
    for i in range(len(numbers)-1):
        for j in range(i+1, len(numbers)):
            new = numbers[i] + numbers[j]
            if not new in answer:
                answer.append(new)
    answer.sort()
    return answer