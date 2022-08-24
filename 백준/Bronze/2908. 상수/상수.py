numbers = input().split(' ')
a = numbers[0]
b = numbers[1]
reverse_a = int(a[::-1])
reverse_b = int(b[::-1])
if reverse_a > reverse_b:
    print(reverse_a)
else:
    print(reverse_b)