N = int(input())
timeList = list()

for _ in range(N):
    a, b = map(int, input().split(' ')) # a는 시작시간 b는 종료시간
    timeList.append((b, a))               # 튜플을 종료시간으로 정렬하기 위해 종료시간을 앞에 위치시킨다.

timeList = sorted(timeList)

count = 1 # timeList의 첫번째 인덱스 값 카운트
end = 0
next = 1
while next < N:
    if timeList[end][0] <= timeList[next][1]: # 종료시간과 다음 시작시간을 비교한다.
        count += 1
        end = next
    next += 1
print(count)