'''
처음 값은 최소 거리인 1 끝 값은 만들 수 있는 최대 거리
앞 집 부터 공유기를 설치한다고 가정 c개를 넘어가면 더 넓게 설치 할 수 있다는 의미 
설치 거리를 mid + 1로 확장
다시 앞집 부터 설치
c개 미만이면 더 좁게 설치해야 한다는 의미
mid - 1로 줄임
다시 앞집 부터 설치
'''
n, c = map(int, input().split())
nList = []

for _ in range(n):
    nList.append(int(input()))
nList.sort()

def install_router(array, start, end):  
    result = 0  
    while start <= end:
        mid = (start + end) // 2 # 인접한 두 공유기 사이의 거리
        router = array[0]
        cnt = 1
        # mid 만큼의 거리를 가지는 공유기 설치
        for i in range(1, n):
            if array[i] >= router + mid:
                router = array[i]
                cnt += 1
        # 거리 확장 현재까지의 최대 거리 저장
        if cnt >= c:
            start = mid + 1
            result = mid
        else:
            end = mid - 1
    return result
         

start = 1
end = nList[-1] - nList[0]
print(install_router(nList, start, end))