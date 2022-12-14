'''
지원자의 성적이 하나이상 모든 지원자에 대해 우수해야한다.
자신보다 앞선 등수의 사람을 기준으로 다른 하나의 성적이 우수해야함.
'''
import sys

for _ in range(int(sys.stdin.readline().rstrip())): # 20
    n = int(sys.stdin.readline().rstrip())
    score = [0] * (n + 1)
    for _ in range(n):
        a, b = map(int, sys.stdin.readline().rstrip().split())
        score[a] = b
    
    cnt = 1
    top = 1
    # 2번째 순위부터 n 순위까지 확인한다.
    for i in range(2, n + 1): # 1000000
        # 지속적으로 작은 값을 찾아서 저장한다. top에는 현재까지 가장 작은 값을 가지게 된다.
        if score[i] < score[top]:
            top = i
            cnt += 1
    print(cnt)