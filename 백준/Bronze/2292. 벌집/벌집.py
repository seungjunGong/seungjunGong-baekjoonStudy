n = int(input())

step = 1
max = 1
# 방의 갯수 1: 1 2: 2~7 3: 8~19 4: 20~37 5: 38~61 .....

while max < n: # 최댓값안에 값이 있으면 방 갯수 출력
    max += 6 * step # 방의 갯수 별 최댓값 저장
    step += 1
print(step)