N, r, c = map(int, input().split())

def solution(x, y, size, cnt):
    if size == 1:
        print(cnt)
        return
    
    half = size // 2
    area = half * half
    
    if r < x + half and c < y + half:      # 왼쪽 위
        solution(x, y, half, cnt)
    elif r < x + half and c >= y + half:   # 오른쪽 위
        solution(x, y + half, half, cnt + area)
    elif r >= x + half and c < y + half:   # 왼쪽 아래
        solution(x + half, y, half, cnt + area * 2)
    else:                                  # 오른쪽 아래
        solution(x + half, y + half, half, cnt + area * 3)
        
solution(0, 0, 2 ** N, 0)