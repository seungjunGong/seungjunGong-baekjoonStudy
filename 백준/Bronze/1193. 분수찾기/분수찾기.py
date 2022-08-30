X = int(input())
count = 1

while X > count: # 라인 별 카운트 X번째 분수가 있는 대각선 라인 찾기
    X -= count
    count += 1

if count % 2 == 0: # 짝수라인은 감수하고 홀수라인은 증가한다.
    a = X          # 라인의 나머지 값
    b = count - (X-1) # 라인의 수에서 감소한다.
else:
    a = count - (X-1)
    b = X
print(f"{a}/{b}")