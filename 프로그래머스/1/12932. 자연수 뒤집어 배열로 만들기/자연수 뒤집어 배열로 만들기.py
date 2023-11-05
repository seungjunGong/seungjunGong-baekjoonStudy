def solution(n):
    answer = str(n)
    answer = list(map(int, list(answer[::-1])))
    return answer