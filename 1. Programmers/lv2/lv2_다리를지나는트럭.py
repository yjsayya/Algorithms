# def solution(bridge_length, weight, truck_weights):
    
#     answer = 0
#     queue = []
    
#     if len(truck_weights) == 1:
#         return bridge_length + 1
    
#     while len(truck_weights) != 0:
#         queue.append(truck_weights.pop(0))
#         if sum(queue) > weight:
#             truck_weights.insert(0,queue.pop())
#             answer += len(queue) + bridge_length - 1
#             queue.clear()

#         print(queue, truck_weights, end=" ")
#         print(answer)
        
#     answer += len(queue) + bridge_length - 1
#     return answer + 1

# print(solution(2, 10, [7,4,5,6]))


from collections import deque

def solution1(bridge_length, weight, truck_weights):

    dq = deque([0]*weight,maxlen=bridge_length)
    cnt = 0

    while len(truck_weights) != 0:
        if sum(dq) <= weight:
            dq.append(truck_weights.pop(0))
            cnt += 1
        else:
            dq.append(0)
            cnt += 1
    return cnt + bridge_length + 1

print(solution1(2, 10, [7,4,5,6]))