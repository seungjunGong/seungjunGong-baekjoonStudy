def solution(sequence, stack, m):
    if len(stack) == m:
        print(" ".join(map(str, map(lambda i: sequence[i], stack))))
        return

    prev = 0    
    for i in range(len(sequence)):
        if prev != sequence[i] and (not stack or i >= stack[-1]):
            stack.append(i)
            solution(sequence, stack, m)
            prev = sequence[stack.pop()]

n, m = map(int, input().split())
sequence = sorted(list(map(int, input().split())))
solution(sequence, [], m)