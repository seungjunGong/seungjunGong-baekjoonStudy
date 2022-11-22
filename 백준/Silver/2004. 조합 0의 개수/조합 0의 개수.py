n, m = map(int, input().split(' '))

nCnt_f = 0
mCnt_f = 0
n_mCnt_f = 0
nCnt_t = 0
mCnt_t = 0
n_mCnt_t = 0

## 끝자리 0 == 10의 배수
## 5의 배수, 2의 배수 구함 
## 5의 배수를 더 빠르게 구하는 법
## 5의 배수 25의 배수 125의 배수... 으로 구해서 팩토리얼에서의 0의 개수를 구함 
## 함수로 만들어 풀면 더 깔끔할 듯..
 
five = 5
while five <= n:
    nCnt_f += n // five
    five *= 5

five = 5
while five <= m:
    mCnt_f += m // five
    five *= 5

five = 5
while five <= n-m:
    n_mCnt_f += (n-m) // five
    five *= 5

two = 2
while two <= n:
    nCnt_t += n // two
    two *= 2

two = 2
while two <= m:
    mCnt_t += m // two
    two *= 2

two = 2
while two <= n-m:
    n_mCnt_t += (n-m) // two
    two *= 2

resFive = nCnt_f - (mCnt_f + n_mCnt_f)
resTwo = nCnt_t - (mCnt_t + n_mCnt_t)

print(min(resTwo, resFive))