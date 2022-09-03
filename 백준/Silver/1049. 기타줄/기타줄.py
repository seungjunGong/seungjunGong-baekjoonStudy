N, M = map(int, input().split(' '))
brand = [list(map(int, input().split())) for _ in range(M)]
pack = 1001
line = 1001
count = 0
for b in brand:          # 패키지, 한줄씩 사는 것의 최소값 구하기
    if b[0] < pack:
        pack = b[0]
    if b[1] < line:
        line = b[1]  
while N >= 6:             # N이 6보다 클경우
    N -= 6                
    if pack < 6 * line:   
        count += pack
    else:                   # 한줄씩 6개 산 것이 6줄 패키지로 산것 보다 싸면
        count += 6 * line        
if N > 0 and pack < N * line:         # 나머지 수에서 패키지가 더 싸면
    count += pack
elif N > 0:
    count += line * N
print(count)