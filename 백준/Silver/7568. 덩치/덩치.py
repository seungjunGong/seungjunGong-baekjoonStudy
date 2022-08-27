n = int(input())
x = list()
y = list()
k = list()
# 몸무게 키 값 받아오기
for i in range(n):
    x_y = input().split(' ')
    x.append(int(x_y[0])) 
    y.append(int(x_y[1]))
    k.append(0)
# 더 큰 덩치의 사람이 k명이면 등수는 k+1임
for i in range(n):
    for j in range(n):
        if x[i] < x[j] and y[i] < y[j]:
            k[i] += 1
for rank in k:
    print(rank+1)
