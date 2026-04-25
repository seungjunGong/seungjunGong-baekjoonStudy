N, S = map(int, input().split())
arr = list(map(int, input().split()))

cnt = 0
def solution(depth, curr):
    global cnt
    if depth == N:
        if curr == S:
            cnt += 1
        return 
    
    # 더하기
    solution(depth + 1, curr + arr[depth])
    # 안 더하고 건너 뛰기
    solution(depth + 1, curr)

solution(0, 0)

if S == 0:
    cnt -= 1
print(cnt)