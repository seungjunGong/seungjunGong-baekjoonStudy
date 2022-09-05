dice = sorted(list(map(int, input().split(' '))))
#3 6 6
A = dice[0]
B = dice[1]
C = dice[2]

if A == B and B == C and A == C:
    print(10000 + A * 1000)
elif A == B or B == C:
    print(1000 + B * 100)
else:
    print(C * 100)