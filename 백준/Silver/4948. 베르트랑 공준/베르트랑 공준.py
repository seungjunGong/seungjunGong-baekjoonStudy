n = 123456
counts = list()
is_prime = [True for _ in range(246913)]

is_prime[0] = False
is_prime[1] = False

i = 2
while i < int(246912 ** 0.5)+1: # 2n의 최대값까지 소수 구하기
    j = 2
    while i * j < 246913:
        if is_prime[i*j]:
            is_prime[i*j] = False
        j += 1
    i += 1

while 1:                        # n + 1부터 2n까지의 소수 개수 구하기
    n = int(input())
    count = 0
    if n == 0:
        break
    for k in range(n+1, 2 * n + 1):
        if is_prime[k]:
            count += 1
    counts.append(count)

for count in counts:
    print(count)