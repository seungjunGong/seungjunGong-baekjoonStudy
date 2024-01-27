def fib(n):
    global cnt
    if (n == 1 or n == 2):
        cnt += 1
        return 1
    else:
        return fib(n-1)+fib(n-2)

n = int(input())
global cnt
cnt = 0
fib(n)
print(cnt, n - 2)