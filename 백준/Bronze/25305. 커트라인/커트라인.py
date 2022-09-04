N, k = map(int, input().split(' '))
x = list(map(int, input().split(' ')))
x.sort()                     # int 형만 정상적으로 정렬시킨다.
print(x[-k])