n, m = map(int, input().split())
memo = dict()
for i in range(n):
    site, pw = input().split()
    memo[site] = pw

for i in range(m):
    site = input()
    print(memo[site])