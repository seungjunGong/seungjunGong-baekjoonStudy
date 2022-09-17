A, B = input().split()

maxA, maxB = int(A.replace('5', '6')), int(B.replace('5', '6'))
minA, minB = int(A.replace('6', '5')), int(B.replace('6', '5'))

print(f"{minA+minB} {maxA+maxB}")