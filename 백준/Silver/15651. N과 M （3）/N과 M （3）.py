def solution(stack, n, m):
    if len(stack) == m:
        print(" ".join(map(str, stack)))
        return

    for i in range(1, n+1):
        stack.append(i)
        solution(stack, n, m)
        stack.pop()
n, m = map(int, input().split())
solution([], n, m)