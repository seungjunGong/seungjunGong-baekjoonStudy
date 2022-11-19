T = int(input())

for _ in range(T):
    N, M = map(int, input().split(' '))
    topfactorial = 1
    bttfactorial = 1

    for top in range(M, M-N, -1):
        topfactorial *= top

    for btt in range(N, 0, -1):
        bttfactorial *= btt

    print(topfactorial // bttfactorial)  