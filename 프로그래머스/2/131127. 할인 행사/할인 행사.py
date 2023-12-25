def solution(want, number, discount):
    answer = 0
    
    products = discount[:10].copy()
    calc = {want[i] : number[i] for i in range(len(want))}
    
    for product in products:
        if product in want:
            calc[product] -= 1
    
    checking = lambda c : len(list(filter(lambda x: x <= 0, c.values()))) == len(want)
    
    if checking(calc):
        answer += 1
            
    for i in range(10, len(discount)):
        out_p, in_p = products.pop(0), discount[i] 
        products.append(discount[i])
        
        if out_p in want:
            calc[out_p] += 1
        
        if in_p in want:
            calc[in_p] -= 1
                 
        if checking(calc):
            answer += 1            
        
    return answer