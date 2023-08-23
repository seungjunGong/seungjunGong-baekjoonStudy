n = int(input())
broken = []
channel = 100
cnt = abs(100 - n)
k = int(input())

if k != 0:
    broken = list(map(int, input().split()))
for number in range(1000001):
    numbers = str(number)
    
    for i in range(len(numbers)):
        if int(numbers[i]) in broken:
            break
        elif i == len(numbers) - 1:
            cnt = min(cnt, abs(int(numbers) - n) + len(numbers))
print(cnt)