T = int(input())
com_num = list()
remainder = {1:'1111', 2:"2486", 3:"3971", 4:"4646", 5:'5555', 6:'6666', 
7:"7931", 8:"8426",9: "9191"}
for case in range(T):
    ab = input().split(" ")
    a = int(ab[0])
    b = int(ab[1]) % 4
    if a % 10 == 0:
        com_num.append(10)
    else:
        com_num.append(remainder[a%10][b-1])

for num in com_num:
    print(num)