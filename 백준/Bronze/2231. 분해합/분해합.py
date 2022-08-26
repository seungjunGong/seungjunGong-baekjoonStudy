n = int(input())

result = n
min = list()
for num in range(n):
    num_lis = [int(x) for x in str(num)]
    result = num + sum(num_lis)
    if result == n:
        min.append(num)
if min:
    print(min[0])
else:
    print(0)