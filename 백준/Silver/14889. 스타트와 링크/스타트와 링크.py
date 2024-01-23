N = int(input())
ability = [list(map(int, input().split())) for _ in range(N)]
ans = 100 * 20

def calc(team_A):
    A, B = 0, 0
    team_B = [i  for i in range(N) if i not in team_A]
    
    for ai, bi in zip(team_A, team_B):
        for aj, bj in zip(team_A, team_B):
            A += ability[ai][aj]
            B += ability[bi][bj]
    return abs(A-B)

def half(stack):
    global ans
     
    if len(stack) == N//2:
        ans = min(ans, calc(stack))
        return
    
    for i in range(N):
        if (not stack or stack[-1] > i):
            stack.append(i)
            half(stack)
            stack.pop()

half([])
print(ans)