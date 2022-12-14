import heapq
n = int(input())

plus = []
minus = []
for _ in range(n):
    read = int(input())
    if read < 1:
        minus.append(read)
    else:
        plus.append(read)
minus.sort()
plus.sort()    

result = 0
fasteningPlus = []
fasteningMinus = []
for i in minus:
    if len(fasteningMinus) == 2:
        result += (fasteningMinus[0] * fasteningMinus[1])
        fasteningMinus = []
    if i < 0:
        fasteningMinus.append(i)
    elif i == 0 and len(fasteningMinus) == 1:
        fasteningMinus = []

for i in range(len(plus)-1, -1, -1):
    if len(fasteningPlus) == 2:
        result += (fasteningPlus[0] * fasteningPlus[1])
        fasteningPlus = []
    if plus[i] == 1:
        result += plus[i]
    else:
        fasteningPlus.append(plus[i])

if len(fasteningMinus) == 2:
    result += (fasteningMinus[0] * fasteningMinus[1])
elif len(fasteningMinus) == 1:
   result += fasteningMinus[0]
if len(fasteningPlus) == 2:
    result += (fasteningPlus[0] * fasteningPlus[1])
    fasteningPlus = []
elif len(fasteningPlus) == 1:
   result += fasteningPlus[0]
   
print(result)