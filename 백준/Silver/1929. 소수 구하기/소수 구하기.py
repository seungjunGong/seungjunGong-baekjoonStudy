m_n = input().split(' ')
m = int(m_n[0])
n = int(m_n[1])

prime_list = [True for _ in range(n+1)]
prime_list[0] = False
prime_list[1] = False

for i in range(2,n+1):
    j = 2
    while prime_list[i] and i * j < n+1: # 2의 배수삭제 3의 배수 삭제 겹치는 배수 삭제
        prime_list[i * j] = False
        j += 1

for i in range(m, n+1):
    if prime_list[i]:
        print(i)    