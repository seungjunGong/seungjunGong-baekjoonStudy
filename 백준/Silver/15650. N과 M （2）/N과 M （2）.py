def solution(stack, n, m):
    if len(stack) == m:
        print(" ".join(map(str, stack)))
        return
    for i in range(1, n+1):
        if not stack or stack[-1] < i:
            stack.append(i)
            solution(stack, n, m)
            stack.pop()

'''
배열 이용 풀이
def solution(stack, start, index, n, m):
    if index == m:
        print(" ".join(map(str, stack)))
        return
    for i in range(start, n+1):
        stack[index] = i
        solution(stack, i+1, index+1, n, m)
n, m = map(int, input().split())
stack = [0 for _ in range(m)]
solution(stack, 1, 0, n, m)
'''

n, m = map(int, input().split())
solution([], n, m)