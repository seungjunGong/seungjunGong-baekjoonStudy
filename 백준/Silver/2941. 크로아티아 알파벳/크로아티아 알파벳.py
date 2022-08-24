alp = ['c=','c-','dz=','d-','lj','nj','s=','z=']
croatia_alp = input()
for word in alp:
    croatia_alp = croatia_alp.replace(word, 'o')  # replace() 문자열안의 단어를 찾아 변환해주는 함수               
print(len(croatia_alp))