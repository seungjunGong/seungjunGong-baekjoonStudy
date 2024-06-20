def solution(n, money):
    answer = 0
    
    dp = [1] + [0] * n
    
    for coin in money:
        for price in range(coin, n+1):
            dp[price] += dp[price - coin]
    
    answer = dp[n] % 1000000007
    return answer