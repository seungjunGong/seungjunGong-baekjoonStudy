t = int(input())
new_s = list()

for i in range(t):
    case = list()
    sum = ''
    case = input().split(" ")
    r = int(case[0])
    s = case[1]
    for c in s:
        sum += c * r
    new_s.append(sum)

for n in new_s:
    print(n)