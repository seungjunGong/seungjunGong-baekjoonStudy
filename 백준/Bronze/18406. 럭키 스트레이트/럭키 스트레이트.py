N = input()
mid = len(N) // 2

left = 0
right = 0

for number in N[:mid]:
    left += int(number)
for number in N[mid:]:
    right += int(number)

print("LUCKY" if left == right else "READY")