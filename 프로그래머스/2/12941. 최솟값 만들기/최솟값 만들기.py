def solution(A,B):
    answer = 0

    A_sort = sorted(A)
    B_sort = sorted(B, reverse=True)
    
    answer = sum([A_sort[i] * B_sort[i] for i in range(len(A))])
    return answer