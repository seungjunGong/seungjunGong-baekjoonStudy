number = [int(input()) for _ in range(5)]
number.sort()

print(f"{sum(number)//5}\n{number[2]}")