# 그리디 알고리즘
# 파이썬 정렬 -> 리스트 내의 작은 수로 정렬
# 1. shot 2. shot 기준 line의 끝점까지 모든 라인 생략 3. 끝점 부터 shot
def solution(targets):
    answer = 0
    
    targets.sort()
    shot = 0
    
    for start, end in targets:
        if start < shot:
            if end < shot:
                shot = end
        else:
            answer += 1
            shot = end
    
    return answer