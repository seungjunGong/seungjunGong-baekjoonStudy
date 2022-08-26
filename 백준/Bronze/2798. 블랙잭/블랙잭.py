n_m = input().split(' ')
cards = input().split(' ')
n = int(n_m[0]) # 카드 개수
m = int(n_m[1]) # 주어진 수
cards = [int(i) for i in cards]
sum = 0
for a in cards:
    for b in cards:
        for c in cards:
            if a != b and b != c and a != c:
                if sum < a+ b + c and a + b + c <= m:
                    sum = a + b + c 
print(sum)