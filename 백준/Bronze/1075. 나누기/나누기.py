N = input()
F = int(input())
N = N[:-2]
second = 0
first = 0
result = ''
while 1:
    if int(N + str(second) + str(first)) % F == 0:
        result = str(second) + str(first)
        break
    if first < 9:
        first += 1
    else:
        second += 1
        first = 0
print(result)