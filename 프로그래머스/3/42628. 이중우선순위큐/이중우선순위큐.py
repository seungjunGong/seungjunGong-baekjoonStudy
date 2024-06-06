
def solution(operations):
    sortL = []
    
    for oper in operations:
        command, num = oper.split(' ')
        if command == 'I':
            sortL.append(int(num))
        else:
            if not sortL:
                continue
            if int(num) == 1:
                del sortL[-1]
            else:
                del sortL[0]
        sortL.sort()
    
    answer = [0, 0]
    if sortL:
        answer = [sortL[-1], sortL[0]]
    
    return answer