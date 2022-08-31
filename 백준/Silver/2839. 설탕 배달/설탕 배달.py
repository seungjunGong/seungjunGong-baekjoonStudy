N = int(input()) # kg
count = 0
while N > 0:
    if N % 5 == 0: # 5kg을 최우선으로 계산함
        count += N // 5
        N = 0 
    else:          # 3kg씩 뺸다.
        N -= 3
        count += 1
if N < 0:          # 0으로 끝나지 않으면 N킬로그램 만들수 없다.
    print(-1)
else:
    print(count)