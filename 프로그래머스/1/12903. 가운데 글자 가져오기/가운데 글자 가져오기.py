def solution(s):
    mid = len(s)//2
    answer = s[mid:mid+1] if len(s) % 2 == 1 else s[mid-1:mid+1] 
    return answer