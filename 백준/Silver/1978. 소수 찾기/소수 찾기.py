n = int(input())
num = input().split(" ")
num = list(map(int,num))
count = 0
for i in range(n):
    if num[i] == 1:
        count += 1
        continue
    for k in range(2,num[i]):
        if num[i] % k == 0:
            count += 1
            break
print(n - count)