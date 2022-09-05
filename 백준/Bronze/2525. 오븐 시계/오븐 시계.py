A, B = map(int, input().split(' '))
C = int(input())

if B + C < 60:
    B += C
else:
    A += C // 60
    if B + (C % 60) >= 60:
        A += 1
        B += C % 60 - 60
    else:
        B += C % 60 
    if A > 23:
        A -= 24

print(f"{A} {B}")