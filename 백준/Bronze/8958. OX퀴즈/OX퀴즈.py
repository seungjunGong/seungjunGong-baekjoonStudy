n = int(input(""))
scores = list()
for i in range(n):
    ox = input("")
    count = 0
    sum = 0
    if ox[0] == 'O':
        count = 1
        sum = count
    for k in range(1,len(ox)): 
        if (ox[k-1] == ox[k] and ox[k] == 'O'):
            count += 1
            sum += count
        elif (ox[k] == 'O'):
            count = 1
            sum += count
    scores.append(sum)

for score in scores:
    print(score)