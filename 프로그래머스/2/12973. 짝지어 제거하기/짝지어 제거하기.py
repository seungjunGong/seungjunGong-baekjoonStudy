def check_alp(stack):
    if len(stack) >= 2:
        if stack[-1] == stack[-2]:
            stack.pop()
            stack.pop()
                
def solution(s):
    
    answer = 1
    stack = []
    
    for alp in s:
        check_alp(stack)
        stack.append(alp)
    
    check_alp(stack)
    
    if stack:
        answer = 0
        
    return answer 