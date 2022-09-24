S = input()

count = list()

index = 1
for end in range(len(S),0, -1):
    for i in range(end):
        count.append(S[i:i+index])
    index += 1

print(len(set(count)))