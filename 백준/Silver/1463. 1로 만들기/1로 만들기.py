N = int(input())
num = [0 for _ in range(N+1)]

for i in range(2,N+1):
    A,B,C = 999999, 999999, 999999
    if i % 3 == 0:
        A = num[int(i/3)]
    if i % 2 == 0:
        B = num[int(i/2)]
    C = num[int(i-1)]
    num[i] = min(A, B, C) + 1

print(num[N])