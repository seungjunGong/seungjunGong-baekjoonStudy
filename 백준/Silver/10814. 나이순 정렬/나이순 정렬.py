N = int(input())

join = [input().split(' ') for _ in range(N)]

join.sort(key = lambda tup: int(tup[0])) # 튜플의 0번 인덱스를 기준으로 정렬한다.

for age, name in join:
    print(f"{age} {name}")