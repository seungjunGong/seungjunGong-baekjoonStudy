N, M = map(int, input().split( ))
wbList = list()
wList = "WBWBWBWB"
bList = "BWBWBWBW"
wwList = [wList, bList, wList, bList, wList, bList, wList, bList] # w가 먼저 나왔을 때 리스트
bbList = [bList, wList, bList, wList, bList, wList, bList, wList] # b가 먼저 나왔을 때 리스트 총 8 X 8
counts = list()
length = N
width = M
for i in range(length):
    wbLine = input()
    wbList.append(wbLine)

# 맨 오른쪽 아래 부터 찾기 시작
while M >= 8:
    N = length # 오른쪽 아래부터 찾고 난후 한칸 왼쪽으로 간뒤 다시 아래부터 찾기
    while N >= 8:
        count = 0
        wwbb = 0
        for n in range(N-8, N):
            wb = 0
            for m in range(M-8, M):
                if wbList[N-8][M-8] == 'W':          # 첫번째 칸이 W이면 계속 wwList로 찾기          
                    if wbList[n][m] != wwList[wwbb][wb]:
                        count += 1
                else:
                    if wbList[n][m] != bbList[wwbb][wb]:
                        count += 1
                wb += 1
            wwbb += 1 
        counts.append(count)
        N -= 1
    M -= 1

M = width
N = length
# 맨 오른쪽 아래 부터 찾기 시작
while M >= 8:
    N = length # 오른쪽 아래부터 찾고 난후 한칸 왼쪽으로 간뒤 다시 아래부터 찾기
    while N >= 8:
        count = 0
        wwbb = 0
        for n in range(N-8, N):
            wb = 0
            for m in range(M-8, M):
                if wbList[N-8][M-8] == 'B':          # 첫번째 칸이 B이면 계속 wwList로 찾기          
                    if wbList[n][m] != wwList[wwbb][wb]:
                        count += 1
                else:
                    if wbList[n][m] != bbList[wwbb][wb]:
                        count += 1
                wb += 1
            wwbb += 1 
        counts.append(count)
        N -= 1
    M -= 1

print(min(counts))