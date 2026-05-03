T = int(input())

for test_case in range(1, T + 1):
    A, B, N = map(int, input().split())
     
    count = 0
    while max(A, B) <= N:
        if A < B:
            A += B  # 작은 값에 큰 값을 더해야 다음 증가량도 커짐
        else:
            B += A
        count += 1
    print(count)