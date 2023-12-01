'''
bandage = [기술 시전 시간, 1초당 회복량, 추가 회복량]
attacks = [공격시간, 피해량]
'''
def solution(bandage, health, attacks):
    answer = 0
    time = 0                    # 현재 시간
    band_time = 0               # 붕대 감는 시간
    hp = health                 # 현재 체력
    end_time = attacks[-1][0]   # 종료 시간
    
    while(time < end_time and hp > 0): # 종료시간, 체력 체크 
        time += 1
        if time == attacks[0][0]:   # 공격 받은 경우
            hp -= attacks[0][1]
            del attacks[0]
            band_time = 0
        else:                       # 밴드 감는 경우     
            band_time += 1
            hp = min(health, hp + bandage[1])         # 1초 회복, 최대 체력 보정
            if band_time == bandage[0]:               # 추가 회복
                hp = min(health, hp + bandage[2])     # 추가 회복, 체력 보정
                band_time = 0
    
    answer = hp if hp > 0 else -1
    return answer