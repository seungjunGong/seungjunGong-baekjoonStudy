def solution(n, lost, reserve):
    students = [1 for _ in range(n+2)]
    
    self_recovered = set(lost) & set(reserve) # 여벌이 있는데 도난당한 경우 처리 X
    
    # 도난된 학생 저장
    for i in lost:
        if i in self_recovered:
            continue
        students[i] = 0
    
    # 체육복 빌려주기
    for i in sorted(reserve):
        if i in self_recovered: # 여벌이 있는데 도난 당한 경우
            continue
            
        if students[i-1] == 0: # 앞 번호에게 빌려주기
            students[i-1] = 1
        elif students[i+1] == 0: # 뒷 번호에게 빌려주기
            students[i+1] = 1
    answer = sum(students[1:n+1])
    
    return answer