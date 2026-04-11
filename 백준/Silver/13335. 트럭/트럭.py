from collections import deque

n, w, L = map(int, input().split())
trucks = list(map(int, input().split()))

time = 0
bridge = [0] * w
current_weight = 0
truck_idx = 0

while truck_idx < n or current_weight > 0:
    time += 1
    
    # 다리 이동
    out_truck = bridge.pop(0)
    current_weight -= out_truck
    
    # 트럭 이동 여부
    if truck_idx < n and current_weight + trucks[truck_idx] <= L:
        bridge.append(trucks[truck_idx])
        current_weight += trucks[truck_idx]
        truck_idx += 1
    else:
        bridge.append(0)
print(time)
