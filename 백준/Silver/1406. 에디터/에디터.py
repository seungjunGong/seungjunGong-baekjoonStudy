LStack = list(input())
RStack = list()
m = int(input())

for _ in range(m):
    commend = input().split()
    if commend[0] == 'L':
        if(LStack):
            RStack.append(LStack.pop())
    elif commend[0] == 'D':
        if(RStack):
            LStack.append(RStack.pop())
    elif commend[0] == 'B':
        if(LStack):
            LStack.pop()
    elif commend[0] == 'P':
        LStack.append(commend[1])

res = "".join(LStack) + "".join(reversed(RStack))

print(res)