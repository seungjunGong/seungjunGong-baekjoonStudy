n = int(input())

def is_prime(num):
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

for _ in range(n):
    num = int(input())

    if num < 2:
        print(2)
    else:
        while(not is_prime(num)):
            num += 1
        print(num)