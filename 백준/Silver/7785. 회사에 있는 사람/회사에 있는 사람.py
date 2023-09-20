n = int(input())
logs = {}

for _ in range(n):
    name, log = input().split()
    if name in logs:
        logs.pop(name)
        continue
    logs[name] = log

reversed_logs = reversed(sorted(logs.keys()))
for name in reversed_logs:
    print(name)