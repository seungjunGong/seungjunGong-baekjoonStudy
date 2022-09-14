from collections import Counter
import sys
N = int(sys.stdin.readline())

number = [int(sys.stdin.readline()) for _ in range(N)]
number.sort()
modeList = Counter(number).most_common(2)

result1 = round(sum(number) / N)
result2 = number[int(N/2)]
if len(modeList) == 2 and modeList[0][1] == modeList[1][1]: 
    result3 = modeList[1][0]
else:
    result3 = modeList[0][0]
result4 = number[-1] - number[0]

print(result1)
print(result2)
print(result3)
print(result4)