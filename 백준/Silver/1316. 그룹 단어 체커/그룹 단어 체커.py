n = int(input())

count = 0
for i in range(n):
    check = True
    in_word = dict()
    word = input()
    for c in range(len(word)):
        in_word[word[c]] = in_word.get(word[c], 0)+1 
        if (in_word[word[c]] > 1) and (word[c] != word[c-1]): # 문자 중복, 연속되지 않을시 count x 
            check = False
            break
    if check:
        count += 1
print(count)