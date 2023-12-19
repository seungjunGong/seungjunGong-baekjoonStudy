def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

def solution(arr):
    arr.sort()
    answer = arr[0]
    
    for i in range(1, len(arr)):
        answer = (arr[i] * answer) // gcd(arr[i], answer) 

    return answer