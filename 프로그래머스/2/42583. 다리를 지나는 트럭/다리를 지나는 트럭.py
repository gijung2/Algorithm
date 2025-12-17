from collections import deque

def solution(bridge_length, weight, truck_weights):
    
    time =0
    waiting = deque(truck_weights)
    bridge = deque([0] * bridge_length)
    bridge_weight = 0
    
    while waiting or  bridge_weight >0:
        time +=1
        
        passed = bridge.popleft()
        bridge_weight -= passed
        
        if waiting and bridge_weight + waiting[0] <= weight:
            truck = waiting.popleft()
            bridge.append(truck)
            bridge_weight += truck
        else:
            bridge.append(0)
    
    return time