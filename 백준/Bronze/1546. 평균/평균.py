N = int(input())
number = list(map(int, input().split(' ')))
max_num = max(number)

for i in range(N):
    number[i] = number[i] / max_num * 100

print(sum(number)/N)