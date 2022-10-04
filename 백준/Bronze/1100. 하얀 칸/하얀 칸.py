cnt = 0
even = True

for _ in range(8):
    N = list(input())
    for n in range(len(N)):
        if even:
            if n % 2 == 0 and 'F' == N[n]:
                cnt += 1
        else:
            if n % 2 != 0 and 'F' == N[n]:
                cnt += 1
    if even:
        even = False
    else: even = True
print(cnt)