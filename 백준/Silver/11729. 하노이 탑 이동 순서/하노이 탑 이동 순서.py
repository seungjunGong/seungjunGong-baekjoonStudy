def hanoi(N, start, end, other):
    if(N == 0):                     # N개의 원판을 다 쌓으면 종료한다.
        return 
    hanoi(N - 1, start, other, end) # N - 1개의 원판을 목적지가 아닌 곳에 쌓는다.
    print(f"{start} {end}")
    hanoi(N - 1, other, end, start) # N개의 원판을 다시 목적지로 쌓는다.
            
N = int(input())
print(2 ** N - 1) # 수행 과정의 수
hanoi(N, 1, 3, 2)