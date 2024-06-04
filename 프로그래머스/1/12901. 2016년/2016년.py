def solution(a, b):
    answer = ''
    day = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]
    month = [0, 31, 29, 31, 30, 31, 30, 31, 31 , 30, 31, 30, 31]
    
    count = -1
    for i in range(a):
        count += month[i]
    answer = day[(count + b) % 7]
    
    return answer