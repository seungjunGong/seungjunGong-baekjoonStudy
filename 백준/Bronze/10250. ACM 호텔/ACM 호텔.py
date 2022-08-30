T = int(input())
number = list()
for case in range(T):
    H,W,N = map(int, input().split(' '))
    d = '' # data
    if N % H == 0:
        if N // H < 10:
            d = str(H) + '0' + str(N // H)
        else:
            d = str(H) + str(N // H)
    else:
        if N // H + 1 < 10:
            d = str(N%H) + '0' + str(N//H + 1)
        else:
            d = str(N%H) + str(N//H + 1)
    number.append(d)

for num in number:
    print(num)