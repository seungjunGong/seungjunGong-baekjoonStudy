n = input()

digit = len(n)
cnt = (int(n) - ((10 ** (digit-1)) -1)) * digit

for i in range(digit - 1 , 0, -1):
    cnt += i * ((10 ** i) - int((10 ** i)/10))

print(cnt)