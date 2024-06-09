"""
query 순회
짝수 인덱스: query[i] 번 인덱스 제외 배열의 query[i] 앞부분(포함)
홀수 인덱스: query[i] 번 인덱스 제외 배열의 query[i] 뒷부분
"""
def solution(arr, query):
    answer = []

    for i in range(len(query)):
        if i % 2 == 0:
            arr = arr[:query[i]+1]
        else:
            arr = arr[query[i]:]
            
    answer = arr
    return answer