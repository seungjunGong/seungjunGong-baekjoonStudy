def solution(left, right):
    divisors = [1 for _ in range(left, right+1)]
    answer = 0
    
    for i in range(left, right+1):
        for j in range(1, i//2+1):
            if i % j == 0:
                divisors[i - left] += 1
    
    for num in range(left, right+1):
        if divisors[num - left] % 2 == 0:
            answer += num
        else: answer -= num
    return answer