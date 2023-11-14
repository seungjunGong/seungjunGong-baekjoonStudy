def solution(brown, yellow):
    answer = []
    
    area = brown + yellow
    width, length = area // 3, 3
    
    while(width > length):
        if (width-2) * (length-2) == yellow:
            break;
        length += 1
        width = area // length
        
    answer = [width, length]

    return answer