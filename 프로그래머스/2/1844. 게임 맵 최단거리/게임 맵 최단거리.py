from collections import deque

def out_maps(x, y, maps):
    return (-1 < x < len(maps)) and (-1 < y < len(maps[0]))

def bfs_mat(maps, v):
    queue = deque([v])
    move_to = [(1, 0), (-1, -0), (0, -1), (0, 1)]
    
    max_size = 100 * 100 + 1
    result = max_size
    
    while(queue):
        x, y, move = queue.popleft()
        
        for mx, my in move_to:
            if (out_maps(x+mx, y+my, maps) and maps[x+mx][y+my]):
                queue.append((x+mx, y+my, move+1))
                maps[x+mx][y+my] = 0
    
        if x == len(maps)-1 and y == len(maps[0])-1:
            result = min(result, move)
    
    return -1 if result == max_size else result
        
def solution(maps):
    answer = bfs_mat(maps, (0,0,1))
    
    return  answer