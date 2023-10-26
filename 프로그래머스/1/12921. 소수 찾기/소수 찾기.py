def solution(n):
    answer = 0
    max_size = 1000001
    is_prime = [True for _ in range(max_size)]
    
    for i in range(2, int(max_size**0.5)+1):
        if is_prime[i]:
            for j in range(i*i, max_size, i):
                is_prime[j] = False
   
    for i in range(2, n+1):
        if is_prime[i]:
            answer += 1
        
    return answer