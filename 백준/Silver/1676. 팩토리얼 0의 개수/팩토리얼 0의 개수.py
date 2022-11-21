factorial = 1

for i in range(int(input()), 0, -1):
    factorial *= i

sFactorial = str(factorial)
cnt = 0

for num in range(1, len(sFactorial)):
    if sFactorial[-num] != '0':
        break
    else: cnt += 1

print(cnt)