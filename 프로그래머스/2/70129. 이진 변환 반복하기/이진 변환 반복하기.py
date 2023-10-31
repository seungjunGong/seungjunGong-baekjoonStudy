def solution(s):
    zero_count, one_count, count = 0, 0, 0
    
    while(len(s) > 1):
        one_count = s.count('1')

        zero_count += len(s) - one_count
        count += 1

        s = str(format(one_count, 'b'))
        
    return [count, zero_count]