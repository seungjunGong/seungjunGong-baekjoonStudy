N = int(input())
prime = list(map(int, input().split(' ')))

if N != 1:
    print(min(prime) * max(prime))
else:
    print(prime[0] * prime[0])