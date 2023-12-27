def solution(arr1, arr2):
    answer = []
    
    for i in range(len(arr1)):
        row = []
        
        for k in range(len(arr2[0])):
            res = 0
            for j in range(len(arr1[i])):
                res += arr1[i][j] * arr2[j][k]
            row.append(res)
            
        answer.append(row)
    
    return answer