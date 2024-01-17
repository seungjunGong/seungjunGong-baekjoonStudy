def solution(stack, n, m):
    if len(stack) == m:
        print(" ".join(map(str, stack)))
    for i in range(1, n+1):
        if i not in stack:        # 중복 확인
            stack.append(i)     
            solution(stack, n, m) # 재귀
            stack.pop()           # 백트래킹

n, m = map(int, input().split())
solution([], n, m)