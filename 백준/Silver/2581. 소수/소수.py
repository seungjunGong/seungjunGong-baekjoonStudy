m = int(input())
n = int(input())
count = list() 
for num in range(m, n+1):
    check = True
    if num == 1:
        continue
    for minor_num in range(2, num):
        if num % minor_num == 0:
            check = False
            break
    if check:
        count.append(num)
        
if count:             # list안에 값이 있으면 True를 반환
    print(sum(count)) 
    print(count[0])
else:
    print(-1)