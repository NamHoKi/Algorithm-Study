def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge_truck = []
    while len(truck_weights) > 0 or len(bridge_truck) > 0:
        answer += 1
        for i in range(len(bridge_truck)-1,-1,-1):
            bridge_truck[i][1] += 1
            if bridge_truck[i][1] == bridge_length:
                weight += bridge_truck[i][0]
                bridge_truck.pop(i)
        if len(truck_weights) != 0 and weight - truck_weights[0] >= 0:
            weight -= truck_weights[0]
            truck = truck_weights.pop(0)
            bridge_truck.append([truck,0])
    return answer
