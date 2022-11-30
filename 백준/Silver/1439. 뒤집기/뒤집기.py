S = list(input())
tmp = S[0]
check = False
cnt = 0

for n in S:
    if n != tmp:
        if check:
            check = False
        else:
            cnt += 1
            check = True
        tmp = n
        
print(cnt)