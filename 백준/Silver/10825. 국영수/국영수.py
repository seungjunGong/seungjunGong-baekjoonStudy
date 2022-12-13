n = int(input())
score = []

for _ in range(n):
    name, language, english, math = input().split()
    score.append([name, int(language), int(english), int(math)])

score.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

for result in score:
    print(result[0])