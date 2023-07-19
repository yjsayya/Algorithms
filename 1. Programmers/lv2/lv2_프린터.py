# priorities의 길이가 100 이하이기 때문에 시간 복잡도를 고려하지 않고 풀 수 있었다 

# queue로 풀어내는 것이 가장 좋은 풀이인 것 같다
# deque vs queue의 시간 복잡도는 고려해볼 필요가 있는 것 같다 

# 첫번째로 푼 풀이
def solution(priorities, location):
    cnt = 0
    queue = []

    for idx,ele in enumerate(priorities):
        queue.append([ele,idx])
        
    while True:
        file = queue.pop(0)
        
        if file[0] < max(priorities):
            queue.append(file)
        else:
            cnt += 1
            priorities.remove(max(priorities))
            if file[1] == location:
                break
            
    return cnt

