'''
유저 id의 값으로 마지막에 저장된 닉네임
Enter 혹은 Change 한 값으로 모든 닉네임을 변경하여 저장
'''
def solution(record):
    answer = []
    nickname = dict() 
    logs = []
    
    for message in record:
        m = message.split(" ")
        state, id = m[0], m[1] 
        if state == "Enter" or state == "Change":
            name = m[2]
            nickname[id] = name
        if state != "Change":
            logs.append((id, state))
    
    for log in logs:
        message = nickname[log[0]] + "님이 "
        message += "들어왔습니다." if log[1] == "Enter" else "나갔습니다."
        answer.append(message)
        
    return answer