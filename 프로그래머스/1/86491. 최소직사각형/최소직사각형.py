def solution(sizes):
    answer = 0
    long, short = 0, 0
    
    for size in sizes:
        w, h = size[0], size[1]
        if w > h:
            long, short = max(long, w), max(short, h)
        else:
            long, short = max(long, h), max(short, w)
    
    answer = long * short
    
    return answer