def solution(msg):
    answer = []
    
    alp_index = {chr(i) : i - ord('A') + 1 for i in range(ord('A'), ord('Z') + 1)}
    
    i = 0
    while i < len(msg):
        for j in range(len(msg), i-1, -1):
            if msg[i:j] in alp_index:
                answer.append(alp_index[msg[i:j]])
                alp_index[msg[i:j+1]] = len(alp_index) + 1
                i = j
                break
                
    return answer