from collections import deque

def check_alp(a, b):
    if len(a) != len(b):
        return False
    
    cnt, i = 0, 0
    while(i < len(a) and cnt < 2):
        if a[i] != b[i]:
            cnt += 1
        i += 1
    return False if cnt > 1 else True 

def bfs(words, visited, begin, target):
    
    queue = deque([(begin, 0)])
    
    while(queue):
        v, move = queue.popleft()
        if target == v:
            return move
        for i in range(len(words)):
            if check_alp(v, words[i]) and not visited[i]:            
                visited[i] = True
                queue.append((words[i], move+1))
    return 0
                
def solution(begin, target, words):
    answer = 0
    visited = [False for _ in words]
    answer = bfs(words, visited, begin, target)
    
    return answer