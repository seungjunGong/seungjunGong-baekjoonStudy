def solution(s, skip, index):
    answer = ''
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    
    for letter in skip:
        alphabet = alphabet.replace(letter, '')
    
    s = list(s)
    for i in range(len(s)):
        s[i] = alphabet[(alphabet.find(s[i]) + index) % (len(alphabet))] 
    
    answer = ''.join(s)
    return answer