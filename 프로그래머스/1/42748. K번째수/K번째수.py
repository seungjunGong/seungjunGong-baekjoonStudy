def solution(array, commands):
    answer = []
    
    for c in commands:
        left, right, i = c[0]-1, c[1], c[2]-1
        cut_line = sorted(array[left:right])
        answer.append(cut_line[i])
        
    return answer