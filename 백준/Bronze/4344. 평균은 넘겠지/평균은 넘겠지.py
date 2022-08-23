c = int(input(""))
answers = list()
for i in range(c):
    test = input("")
    test_line = test.split(" ")
    n = int(test_line[0])
    result = 0
    sum = 0
    for k in range(1, n+1):
        sum += int(test_line[k])
    average = sum / n
    for k in range(1,n+1):
        if average < int(test_line[k]):
            result += (100/n)
    answers.append(result)
for answer in answers:
    print(f"{answer:.3f}%")