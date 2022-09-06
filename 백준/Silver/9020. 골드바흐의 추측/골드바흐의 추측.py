T = int(input())

is_prime = [False] + [False] + [True for _ in range(9999)]

for i in range(2, 101):                  # 10000까지의 소수 구하기
    if is_prime[i]:                      # for문을 덜 돌릴 수 있다.
        for j in range(i*i, 10001, i): 
            is_prime[j] = False

for _ in range(T):
    prime = list()
    n = int(input())

    plus = n // 2
    minus = n // 2                             # 두 수의 합에서 값이 소수인 것을 찾는다.
    while minus != 1:                          # 중간 값에서부터 값을 찾아나가면 가장 먼저 나오는 값이 가장 차가 작음            
        if is_prime[plus] and is_prime[minus]:         
            print(f"{minus} {plus}")                   
            break
        plus += 1
        minus -= 1