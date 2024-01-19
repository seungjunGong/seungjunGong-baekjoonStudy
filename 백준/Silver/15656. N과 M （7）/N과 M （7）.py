def solution(sequence, stack, m):
    if len(stack) == m:
        print(" ".join(map(str, stack)))
        return

    for i in sequence:
        stack.append(i)
        solution(sequence, stack, m)
        stack.pop()

n, m = map(int, input().split())
sequence = sorted(list(map(int, input().split())))
solution(sequence, [], m)