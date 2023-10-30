def solution(s):
    stack = []
    
    for bracket in s:
        if bracket == "(":
            stack.append("(")
        else:
            if not stack:
                return False
            if stack[-1] == "(":
                stack.pop()
        
    return not stack