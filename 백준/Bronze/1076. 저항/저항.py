multipleList = [10 ** i for i in range(10)]
colorList = ['black','brown','red','orange','yellow','green','blue','violet','grey','white']

result = ''
for i in range(3):
    color = input()
    n = colorList.index(color)
    if i == 2:
        print(int(result) * multipleList[n])
    else: result += str(n)