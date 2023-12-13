def solution(n, arr1, arr2):
    answer = []
    
    for i in range(n):
        line_1 = format(arr1[i], 'b').zfill(n)
        line_2 = format(arr2[i], 'b').zfill(n)
        
        block = ""
        for j in range(n):
            block += '#' if int(line_1[j]) | int(line_2[j]) else " "
        answer.append(block)
         
    return answer