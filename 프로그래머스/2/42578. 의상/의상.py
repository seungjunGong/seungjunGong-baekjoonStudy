def solution(clothes):
    answer = 1
    
    clothes_type = dict() 
    for c in clothes:
        clothes_type[c[1]] = clothes_type.get(c[1], 0) + 1
    
    for count in clothes_type.values():
        answer *= count + 1
        
    answer -= 1
    return answer