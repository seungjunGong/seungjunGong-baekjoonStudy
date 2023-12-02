def solution(arr1, arr2):
    col = range(len(arr1))
    row = range(len(arr1[0]))
    
    answer = [[arr1[i][j] + arr2[i][j] for j in row] for i in col]
    
    return answer