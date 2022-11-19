from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = deque([0] * bridge_length)
    bridge_weight = 0
    trucks = deque(truck_weights)
    while trucks:
        bridge_weight -= bridge.popleft()
        if bridge_weight + trucks[0] <= weight and len(bridge) < bridge_length:
            truck_weight = trucks.popleft()
            bridge.append(truck_weight)
            bridge_weight += truck_weight
        else:
            bridge.append(0)
        answer += 1
    answer += len(bridge)
    return answer