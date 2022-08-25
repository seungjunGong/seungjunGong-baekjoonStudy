n = int(input())
prime_num = 2
results = list()
while n != 1:
    if n % prime_num == 0:
        n /= prime_num
        results.append(prime_num)
        continue
    prime_num += 1

for rel in results:
    print(rel)