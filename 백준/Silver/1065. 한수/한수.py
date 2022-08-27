n = int(input())
count = 0
for num in range(1,n+1):
    number = num
    num = [int(i) for i in str(num)]
    if len(num) <= 2: # 각자리수가 2이하인 수는 전부 등차이다.
        count += 1
    elif num[1] - num[0] == num[2] - num[1]: # 등차가 같은 값만 count
        count += 1
print(count)