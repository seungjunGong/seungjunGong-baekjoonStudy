from collections import deque

def bfs(numbers, target):
    answer = 0
    queue = deque([(0, 0)])  # 초기 상태를 큐에 추가

    while queue:
        current_sum, idx = queue.popleft()

        if idx == len(numbers):
            if current_sum == target:
                answer += 1
        else:
            queue.append((current_sum + numbers[idx], idx + 1))
            queue.append((current_sum - numbers[idx], idx + 1))

    return answer

def solution(numbers, target):
    return bfs(numbers, target)

# 예제 테스트
print(solution([1, 1, 1, 1, 1], 3))  # 5
print(solution([4, 1, 2, 1], 4))      # 2
