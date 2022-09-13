N = list(input())
if len(N) == 1:
    if N[0] == '0':
        N.append('0')
    else:
        N = ['0', N[0]]

originNum = int(N[0] + N[1])
count = 0

while 1:
    sum = str(int(N[0]) + int(N[1]))
    if int(sum) < 10:
        sum = '0' + sum 
    N[0] = N[1]
    N[1] = sum[1]
    count += 1
    if originNum == int(N[0] + N[1]):
        break
print(count)