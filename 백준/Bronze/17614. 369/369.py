n = int(input())

cnt = 0
for i in range(1, n+1):
    numbers = str(i)
    for num in numbers:
        if(num == '3' or num == '6' or num == '9' ):    
            cnt += 1
print(cnt)