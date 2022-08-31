T = int(input())
stair = 0
result = list()
for i in range(T):
    k = int(input())
    n = int(input())
    peple = [i for i in range(0,n+1)] # 0층의 n호수 까지 인원 0은 제외
    stair = 0
    while stair != k: # 층수가 k까지
        for j in range(1,n+1): # 1호 부터 n호까지
            peple[j] += peple[j-1] # 1층 2호 = 0층 1호 + 0층 2호 
        stair += 1
    result.append(peple[n])
for rel in result:
    print(rel)