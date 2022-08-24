n = input().split(" ")
a = int(n[0])
b = int(n[1])
c = int(n[2])
# check = False
# sell = 1
# while True:
#     if b > c:
#         check = True
#         break
#     elif a + b * sell < c * sell:
#         print(sell)
#         break
#     sell += 1
# if check:
#     print(-1)
if b >= c:
    print(-1)
else: 
    print((a // (c-b)) + 1) 