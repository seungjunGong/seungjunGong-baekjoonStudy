t_thousand = dict()
for i in range(1,10001):
    t_thousand[i] = t_thousand.get(i, 0) 
    s = str(i)
    constructor = i
    for k in range(len(s)):
        constructor += int(s[k])
    t_thousand[constructor] = t_thousand.get(constructor, 0) + 1
s_thousand = sorted(t_thousand.items(), key = lambda item: item[0])

for num, count in s_thousand:
    if count == 0:
        print(num)