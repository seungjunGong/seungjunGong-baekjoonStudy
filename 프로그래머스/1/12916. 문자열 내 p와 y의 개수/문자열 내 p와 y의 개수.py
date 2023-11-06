def solution(s):
    s = s.lower()
    
    count = 0
    for sp in s:
        if sp == 'p':
            count += 1
        if sp == 'y':
            count -= 1
    
    if count != 0:
        return False

    return True