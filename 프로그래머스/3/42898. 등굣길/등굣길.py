from collections import deque

def solution(m, n, puddles):
    answer = 0
    
    maps = [[0 for j in range(m)] for i in range(n)]
    
    for puddle in puddles:
        i, j = puddle[1]-1, puddle[0]-1
        maps[i][j] = -1
    
    maps[0][0] = 1
    for i in range(n):
        for j in range(m):
            if maps[i][j] != -1:
                if i+1 < n and maps[i+1][j] != -1:
                    maps[i+1][j] += maps[i][j] % 1000000007
                if j+1 < m and maps[i][j+1] != -1:
                    maps[i][j+1] += maps[i][j] % 1000000007
    
    print(maps)
    answer = maps[n-1][m-1] % 1000000007
    return answer