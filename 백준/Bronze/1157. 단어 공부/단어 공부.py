alp = input()
u_alp = alp.upper() # 모두 대문자로 변경
alphabet = dict()
times = 0
alp_save = ''
for c in u_alp: # 문자열 카운팅
    alphabet[c] = alphabet.get(c, 0) + 1
for alp, count in alphabet.items(): # 문자열 카운트 계산
    if times < count:         # 카운트 많은 것 찾기
        times = count
        alp_save = alp
    elif times == count:      # 카운트 중복 일시 '?' 저장
        alp_save = '?'

print(alp_save)