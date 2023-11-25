def solution(a, b):
    answer = sum([ai * bi for ai, bi in zip(a, b)])
    return answer