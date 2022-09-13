N = int(input())

pi = list(map(int, input().split(' ')))
timeList = list()
time = 0

for i in sorted(pi):
    time += i
    timeList.append(time)
print(sum(timeList))