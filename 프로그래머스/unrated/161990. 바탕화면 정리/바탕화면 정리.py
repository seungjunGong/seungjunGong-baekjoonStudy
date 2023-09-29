def solution(wallpaper):
    answer = []
    lux, luy, rdx, rdy = 51, 51, 0, 0
    for i, line in enumerate(wallpaper):
        for j, room in enumerate(line):
            if room == '#':
                if i < lux:
                    lux = i
                if j < luy:
                    luy = j
                if i > rdx:
                    rdx = i
                if j > rdy:
                    rdy = j
                    
    answer = [lux, luy, rdx+1, rdy+1]
        
    return answer