# 정답 풀이
T = int(input())

arr = list()
state = list()

NOT_VISITED = 0
CYCLE_IN = -1

def run(x):
    cur = x
    
    while(True):
        state[cur] = x # 방문 상태 저장
        cur = arr[cur] # 다음 방문 노드 저장
        
        # 이미 지나간 학생을 또 만난 경우
        if(state[cur] == x):
            # 사이클 처리
            while(state[cur] != CYCLE_IN):
                state[cur] = CYCLE_IN
                cur = arr[cur]
            return 
        # 이전 방문에서 지나간 학생에 도달한 경우
        elif state[cur] != NOT_VISITED:
            return
    
for _ in range(T):
    n = int(input())
    
    arr = [0] + list(map(int, input().split()))
    state = [0 for _ in range(n+1)]
    
    for i in range(1, n+1):
        if state[i] == NOT_VISITED:
            run(i)
    cnt = 0
    for i in range(1, n+1):
        if state[i] != CYCLE_IN:
            cnt += 1
    print(cnt)