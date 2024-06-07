'''
X [연산자] Y = Z
'''
def solution(quiz):
    answer = []
    
    for q in quiz:
        ex = q.split(" ")
        x, y, z = tuple(map(int, [ex[0], ex[2], ex[4]]))
        if ex[1] == '-':
            answer.append("O") if x-y == z else answer.append("X")
        else:
            answer.append("O") if x+y == z else answer.append("X")
            
    return answer