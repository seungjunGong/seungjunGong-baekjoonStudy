S = int(input())
sum = 0
result = S

for i in range(1,S+1):
    sum += i
    if sum == S:
        result = i
        break
    elif S - sum < i + 1:
        result = i
        break

print(result)