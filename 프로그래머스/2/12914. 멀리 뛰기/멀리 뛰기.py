def solution(n):
    answer = 0
    
    dp = [0 for _ in range(n+2)]    
    dp[1], dp[2] = 1, 2
    
    if n > 2:
        for i in range(3, n+1):
            dp[i] = (dp[i-1] + dp[i-2]) % 1234567
        
    answer = dp[n]
    
    return answer