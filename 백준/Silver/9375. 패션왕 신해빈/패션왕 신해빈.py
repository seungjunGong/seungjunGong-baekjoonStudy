T = int(input())

for _ in range(T):
    clothesType = dict()
    n = int(input())
    for _ in range(n):
        clothes, type = input().split(' ')
        clothesType[type] = clothesType.get(type, 0) + 1
        
    result = 1
    for type, cnt in clothesType.items():
        result *= (cnt + 1)
    print(result - 1)