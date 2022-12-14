s = input()
array = [s]

for i in range(1, len(s)):
    array.append(s[i:])

for i in sorted(array):
    print(i)