import sys
sys.setrecursionlimit(10000) # 반복문으로 다시 짜볼것

def coke_problem(a, b, n):
    if int(n // a) <= 0:
        return 0
    get_coke = int(n // a) * b
    n = get_coke + (n % a)
    print(n)
    return get_coke + coke_problem(a, b, n)
    

def solution(a, b, n):
    answer = coke_problem(a, b, n)
    return answer