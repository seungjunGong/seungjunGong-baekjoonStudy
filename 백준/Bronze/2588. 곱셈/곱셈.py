num = int(input())
A,B,C = list(map(int, input()))
print(f"{num * C}\n{num * B}\n{num * A}")
print(num * int(str(A)+str(B)+str(C))) 