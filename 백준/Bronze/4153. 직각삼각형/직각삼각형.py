while 1:
    A,B,C = sorted(map(int, input().split()))
    if A == B == C:
        break    
    
    if C * C == A * A + B * B:
        print("right")
    else:
        print("wrong")