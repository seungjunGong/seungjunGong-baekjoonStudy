def solution(s, n):
    answer = ''
    
    for alp in s:
        if alp.isupper():
            answer += chr(65 + ((ord(alp) - 65 + n) % 26))
        elif alp.islower():
            answer += chr(97 + ((ord(alp) - 97 + n) % 26))
        else:
            answer += alp
    return answer