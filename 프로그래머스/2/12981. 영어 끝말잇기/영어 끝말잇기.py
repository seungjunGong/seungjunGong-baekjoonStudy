def solution(n, words):
    answer = []

    counts = {words[0] : 1}
    fail_idx = 0
    turn = 0
    
    for i in range(1, len(words)):
        word = words[i]
        counts[word] = counts.get(word, 0) + 1
        
        if words[i-1][-1] != words[i][0] or counts[word] > 1:
            print(words[i])
            turn = i // n  + 1
            fail_idx = i % n + 1
            break
        
    answer = [fail_idx, turn]
    return answer