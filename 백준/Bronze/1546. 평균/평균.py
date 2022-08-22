scores = list()
result = 0
num =int(input(""))
score = input("")
scores = score.split(" ")
for i in range(0,len(scores)):
    scores[i] = int(scores[i])
scores.sort()
max = int(scores[-1])
for n in scores:
    result += int(n) / max * 100
print(result/num)