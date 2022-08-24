s = input()
alp_db = dict()
for ascii in range(97,123): # ascii 코드 a~z
    alp_db[chr(ascii)] = alp_db.get(chr(ascii), -1)
for alp in s:
    alp_db[alp] = s.index(alp)

for index in alp_db.values():
    print(index, end=' ')
