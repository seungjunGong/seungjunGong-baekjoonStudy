# 장군개미 5 병점개미 3 일개미 1

def solution(hp):
    answer = 0          # 정답(최소 병력)
    attack = [5, 3, 1]  # 각 개미 군단의 체력
    i = 0               # 개미 군단의 순서
    
    while(hp > 0):                  # 0 이되면 종료
        answer += hp // attack[i]   # 
        hp %= attack[i]
        i+=1
        
    return answer