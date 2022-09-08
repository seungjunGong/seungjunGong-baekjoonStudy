N, K = map(int, input().split())
coin = list()
count = 0

for i in range(N):
    coin.append(int(input()))

for i in range(1,N+1):
    if coin[-i] <= K:
        count += K // coin[-i]
    if K % coin[-i] == 0:
        break
    K %= coin[-i]

print(count)