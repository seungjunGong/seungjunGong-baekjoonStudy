def solution(s):
    answer = len(s)
    
    mid = len(s) // 2 + 1
    
    for divide in range(1, mid):
        compressed = ""
        prev = s[0:divide]
        cnt = 1
        
        for i in range(divide, len(s), divide):
            if prev == s[i:i + divide]:
                cnt += 1
            else:
                compressed += str(cnt) + prev if cnt > 1 else prev
                prev = s[i:i + divide]
                cnt = 1
        compressed += str(cnt) + prev if cnt > 1 else prev
        answer = min(answer, len(compressed))
         
    return answer