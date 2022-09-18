N = input()

# 30의 배수 판정법
# 3의 배수이면서 일의자리가 0인 수
# 3의 배수 판정법 각 자리 수의 합이 3
if '0' in N:              
    N = sorted([int(i) for i in N], reverse=True)
    if sum(N) % 3 == 0:
        print(''.join(str(i) for i in N))
    else:
        print(-1)
else: print(-1)