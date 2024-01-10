def dfs(numbers, target, v, idx):
    global answer
    
    if idx == len(numbers): # n 번째인 경우 종료
        if v == target:		# 조건 만족시 카운트
            answer += 1
        return
    dfs(numbers, target, v+numbers[idx], idx+1) # + 부호 붙이기
    dfs(numbers, target, v-numbers[idx], idx+1) # - 부호 붙이기
    
def solution(numbers, target):
    global answer
    answer = 0
    
    dfs(numbers, target, 0, 0)
    
    return answer