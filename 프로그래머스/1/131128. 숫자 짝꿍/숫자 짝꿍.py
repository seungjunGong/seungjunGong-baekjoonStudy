def solution(X, Y):
    answer = ''
    x_count = [0 for i in range(10)]
    y_count = [0 for i in range(10)]
    
    for num in X:
        x_count[int(num)] += 1
    for num in Y:
        y_count[int(num)] += 1
    
    for i in range(9, -1, -1):
        cnt = 0
        if x_count[i] > 0 and y_count[i] > 0:
            cnt = min(x_count[i], y_count[i])
        answer += (str(i) * cnt)
    
    if answer == "":
        answer = "-1"
    elif answer[0] == '0':
        answer = "0" 
        
    return answer