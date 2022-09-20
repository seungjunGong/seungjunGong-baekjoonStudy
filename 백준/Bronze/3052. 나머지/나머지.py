remainder = dict()
for i in range(0,10):
    num =int(input(""))
    result = str(num % 42)
    remainder[result] = remainder.get(result, 0) + 1
print(len(remainder))