def hanoi_tower(n, start, mid, end, result):
    if n <= 0: return
    hanoi_tower(n-1, start, end, mid, result)
    result.append([start, end])
    hanoi_tower(n-1, mid, start, end, result)
    
def solution(n):
    answer = []
    hanoi_tower(n, 1, 2, 3, answer)
    return answer