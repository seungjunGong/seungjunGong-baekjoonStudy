N = int(input())

distance = list(map(int, input().split()))
price = list(map(int, input().split()))

expenses = price[0]
total = 0

for i in range(1, len(price)):
    total += expenses * distance[i-1]
    if expenses > price[i]:
        expenses = price[i]

print(total)