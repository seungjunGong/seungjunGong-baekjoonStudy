k = int(input())
inequalitys = list(input().split())
arr = [0 for _ in range(10)]
visited = [False for _ in range(10)]
max_num = '000'
min_num = '9876543210'

def cal():
    idx = 0
    global max_num, min_num
    good_num = str(arr[0])
    for sign in inequalitys:
        if sign == '>':
            if arr[idx] < arr[idx+1]:
                return
        else:
            if arr[idx] > arr[idx+1]:
                return
        good_num += str(arr[idx+1])
        idx += 1
    max_num = max_num if int(max_num) > int(good_num) else good_num
    min_num = min_num if int(min_num) < int(good_num) else good_num
   
    return

def dfs(depth):
    if depth == k+1:
        cal()
        return
    
    for i in range(10):
        if not visited[i]:
            visited[i] = True
            arr[depth] = i
            dfs(depth+1)
            visited[i] = False

dfs(0)
print(f"{max_num}\n{min_num}")