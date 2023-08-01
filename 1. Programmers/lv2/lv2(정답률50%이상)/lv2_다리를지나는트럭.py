''''''
"""
    스택/큐 문제 -- 이 문제는 큐로 푸는 문제였다 

    ** sum()은 시간 복잡도 ㅈㄴ 크다는 것을 꼭 알아두자 ㅇㅋ
"""


# 첫번째 풀이 -- 힌트 보고 풀었다
# 테스트 케이스 5번에서만 시간초과가 났다
def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = [0 for _ in range(bridge_length)]

    while truck_weights:
        time += 1
        bridge.pop(0)

        if sum(bridge) + truck_weights[0] <= weight:
            bridge.append(truck_weights.pop(0))
        else:
            bridge.append(0)

    return time + bridge_length


# 두번째 풀이 - 다른 사람이 준 힌트 하나를 더 보고 풀었다
'''
첫번째 풀이에서 테스트케이스5에서 시간초과가 났다고 이야기 했었다
- 그 이유는 sum()과정에서 시간복잡도 손해가 많이 난것인데
- 그에 따라 sum(bridge) 대신 bridge_weight 변수를 따로 두어서
- 시간 복잡도를 크게 줄일 수 있었다 ㅇㅋ
'''


def solution2(bridge_length, weight, truck_weights):
    time = 0
    bridge = [0 for _ in range(bridge_length)]
    bridge_weight = 0

    while truck_weights:
        time += 1
        bridge_weight -= bridge.pop(0)

        if bridge_weight + truck_weights[0] <= weight:
            w = truck_weights.pop(0)
            bridge.append(w)
            bridge_weight += w
        else:
            bridge.append(0)

    return time + bridge_length

# 내가 다시 푼 두번째 풀이 - solution2가 더 깔끔하긴 하네
def solution3(bridge_length, weight, truck_weights):

    bridge = [0] * bridge_length
    bridge_weight = 0

    time = 0
    while truck_weights:
        time += 1
        if bridge[0] != 0:
            bridge_weight -= bridge[0]
        bridge.pop(0)

        if bridge_weight + truck_weights[0] <= weight:
            bridge_weight += truck_weights[0]
            bridge.append(truck_weights.pop(0))
        else:
            bridge.append(0)

    return time + bridge_length
