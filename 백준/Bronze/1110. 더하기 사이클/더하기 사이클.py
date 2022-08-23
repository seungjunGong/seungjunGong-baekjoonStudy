n = input("")
if int(n) < 10:
    n = '0' + n
answer = list()
split = list()
nword = list()
count = 0
split.append([*n])
for i in range(100000000):
    ans = int(split[i][0]) + int(split[i][1])
    if ans < 10:
        answer.append([*("0" + str(ans))])
    else:
        answer.append([*str(ans)])
    nword.append(split[i][1] + answer[i][1])
    count += 1
    if nword[i] == n:
        break
    split.append([*nword[i]])

print(count)