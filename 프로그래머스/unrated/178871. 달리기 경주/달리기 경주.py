def solution(players, callings):
    answer = {}
    
    for pi in range(len(players)):
        answer[players[pi]] = pi
    
    for call_player in callings:
        idx = answer[call_player]
        answer[call_player] -= 1
        answer[players[idx-1]] += 1
        players[idx-1], players[idx] = players[idx], players[idx-1]        
    
    return players