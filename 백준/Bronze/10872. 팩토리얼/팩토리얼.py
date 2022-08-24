def factorial(n):
    if n == 0:
        return 1
    result = n * factorial(n-1)
    return result

n = int(input())
print(factorial(n))