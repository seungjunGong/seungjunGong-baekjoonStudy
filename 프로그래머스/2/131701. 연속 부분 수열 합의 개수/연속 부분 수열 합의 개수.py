def solution(elements):
    answer = 0
    
    length = len(elements)
    numbers = {}
    
    for select in range(1, length+1):
        for i in range(length):
            if i + select > length:
                end = (select+i) % length
                num = sum(elements[:end] + elements[i:length])
            else:
                num = sum(elements[i:i+select])
            
            numbers[num] = numbers.get(num, 0) + 1
    answer = len(numbers)                 
    return answer