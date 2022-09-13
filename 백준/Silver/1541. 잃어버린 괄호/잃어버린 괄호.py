N = input().split('-')

for i in range(len(N)):
    num = list(map(int, N[i].split('+')))
    N[i] = sum(num)

if len(N) == 1:
    print(N[0])
else:
    print(f"{-sum(N) + 2 * N[0]}")
