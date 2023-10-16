def solution(babbling):
    answer = 0
    pronunciation = ["ma", "ye", "aya", "woo"]
    
    for words in babbling:
        idx = 0
        check = True
        privious = ""
        while(check and idx < len(words)):
            current = idx
            for p in pronunciation: 
                if privious != p and words[idx:idx+len(p)] == p:
                    privious = p
                    idx += len(p)
            if current == idx:
                check = False
        if check:
            print(p)
            answer += 1
    return answer