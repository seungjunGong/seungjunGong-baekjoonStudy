number = [int(input()) for _ in range(9)]

max_num = max(number)
max_index = number.index(max_num)

print(max_num)
print(max_index + 1)