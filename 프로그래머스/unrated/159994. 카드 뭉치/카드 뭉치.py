def solution(cards1, cards2, goal):
    answer = ''
    
    cds1_idx = 0
    cds2_idx = 0
    gl_idx = 0
    check = True
    
    while(gl_idx < len(goal)):
        temp = gl_idx
        if cds1_idx < len(cards1) and cards1[cds1_idx] == goal[gl_idx]:
            cds1_idx += 1
            gl_idx += 1
        elif cds2_idx < len(cards2) and cards2[cds2_idx] == goal[gl_idx]:
            cds2_idx += 1
            gl_idx += 1
        if temp == gl_idx:
            check = False
            break
    
    answer = "Yes" if check else "No"
        
    return answer