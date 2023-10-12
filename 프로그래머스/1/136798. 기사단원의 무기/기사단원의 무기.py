def solution(number, limit, power):
    answer = 0
    for num in range(1, number+1):
        cnt = 0
        for i in range(1, int(num**0.5)+1):
            if i * i == num:
                cnt += 1
            elif num % i == 0:
                cnt += 2
        if cnt > limit:
            answer += power
        else:
            answer += cnt
    return answer