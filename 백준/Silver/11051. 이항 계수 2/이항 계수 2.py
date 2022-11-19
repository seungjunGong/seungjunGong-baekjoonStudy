N, K = map(int, input().split(' '))
nFactorial = 1
kFactorial = 1
n_kFactorial = 1

for n in range(N, 0, -1):
    nFactorial *= n

for k in range(K, 0, -1):
    kFactorial *= k

for n_k in range(N-K, 0, -1):
    n_kFactorial *= n_k

print(int((nFactorial // (kFactorial * n_kFactorial)) % 10007))