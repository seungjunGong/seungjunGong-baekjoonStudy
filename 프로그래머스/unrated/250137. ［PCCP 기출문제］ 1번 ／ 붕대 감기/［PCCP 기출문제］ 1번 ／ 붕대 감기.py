'''
기술 시전 시간
1초당 회복량
추가 회복량
[공격시간, 피해량]
'''
def solution(bandage, health, attacks):
    answer = 0
    time = 0
    band_time = 0
    mx_hp = health
    end_time = attacks[-1][0]
    
    while(time < end_time and health > 0):
        time += 1
        if time == attacks[0][0]:
            health -= attacks[0][1]
            del attacks[0]
            band_time = 0
        else:
            band_time += 1
            health = min(mx_hp, health + bandage[1])
            if band_time == bandage[0]:
                health = min(mx_hp, health + bandage[2])
                band_time = 0
    
    answer = health if health > 0 else -1
    return answer