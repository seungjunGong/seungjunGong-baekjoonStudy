A, B, V = list(map(int, input().split(" ")))
d = 0 # day
if (V-A) % (A-B) == 0:
    d = (V-A) // (A-B) + 1
else:
    d = (V-A) // (A-B) + 2
print(d)    
