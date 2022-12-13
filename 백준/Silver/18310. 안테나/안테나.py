n = int(input())
house = list(map(int, input().split()))
house.sort()

print(house[(n//2) - 1] if n % 2 == 0 else house[n//2])