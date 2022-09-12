pay = int(input())

change = 1000 - pay
count = 0

while change != 0:
    if change >= 500:
        change -= 500
        count += 1
    elif change // 100 > 0:
        count += change // 100
        change %= 100
    elif change >= 50:
        change -= 50
        count += 1
    elif change // 10 > 0:
        count += change // 10
        change %= 10
    elif change >= 5:
        change -= 5
        count += 1
    else:
        count += change // 1
        change = 0

print(count)