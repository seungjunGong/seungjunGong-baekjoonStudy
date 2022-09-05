H, M = map(int, input().split(' '))

if M - 45 >= 0:
    M -= 45
elif H == 0:
    H = 23
    M = 15 + M
else:
    H -= 1
    M = 15 + M
print(f"{H} {M}")