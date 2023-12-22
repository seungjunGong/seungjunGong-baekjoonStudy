def solution(s):
    answer = 0
    
    b_match = {'[':']', '(':')', '{':'}', ']':0, ')':0, '}':0}
    
    # 괄호 회전
    for turn in range(len(s)):
        stack = []
        turned_b = s[turn:] + s[:turn]
        
        # 괄호 검사
        for b in turned_b:
            if stack and b_match[stack[-1]] == b:
                stack.pop()
            else:
                stack.append(b)
        # 올바른 괄호
        if not stack:
            answer += 1
    
    return answer