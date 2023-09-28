def find_start(park):
     for i in range(len(park)):
        for j in range(len(park[i])):
            if park[i][j] == 'S':
                return (i, j)

def solution(park, routes):    
    h, w = find_start(park) 
    
    for route in routes:
        commend, cnt = route.split()
        cnt = int(cnt)
        check = True
        
        if commend == 'E':
            for i in range(1, cnt+1):
                if w + i >= len(park[w]):
                    check = False
                    break
                if park[h][w+i] == 'X':
                    check = False
                    break
            if check:
                w = w + cnt
        elif commend == 'W':
            for i in range(1, cnt+1):
                if w - i < 0:
                    check = False
                    break
                if park[h][w-i] == 'X':
                    check = False
                    break
            if check:
                w = w - cnt
        elif commend == 'N':
            for i in range(1, cnt+1):
                if h - i < 0:
                    check = False
                    break
                if park[h-i][w] == 'X':
                    check = False
                    break
            if check:
                h = h - cnt
        elif commend == 'S':
            for i in range(1, cnt+1):
                if h + i >= len(park):
                    check = False
                    break
                if park[h+i][w] == 'X':
                    check = False
                    break
            if check:
                h = h + cnt
    answer = [h, w]
                    
    return answer