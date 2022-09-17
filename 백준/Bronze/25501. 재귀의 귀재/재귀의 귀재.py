def recursion(s, l, r, count):
    if l >= r: return 1, count
    elif s[l] != s[r]: return 0, count
    else: return recursion(s, l+1, r-1, count+1)

def isPalindrome(s):
    count = 0
    return recursion(s, 0, len(s)-1, count+1)

T = int(input())

for _ in range(T):
    case = input()
    result, count = isPalindrome(case)
    print(f"{result} {count}")