''''''
"""
<< 스택/큐 문제 >>
   lv1_같은숫자는싫어
   lv2_기능개발 
   lv2_올바른괄호 
   lv2_프로세스
   lv2_다리를지나는트럭 
   lv2_주식가격
   
   
"""
# 1. 같은 숫자는 싫어
def solution(arr):
    stack = []
    for i in arr:
        if stack and stack[-1] != i:
            stack.append(i)
        else:
            stack.append(i)

    return stack


# 2. 기능개발
def solution2(progresses, speeds):
    # 1. 기능 개발
    days = []
    for p ,s in zip(progresses ,speeds):
        if (100-p) %s == 0:
            days.append((100-p)//s)
        else:
            days.append((100-p)//s + 1)
    # 2. 기능 배포
    ans = []
    sta = days.pop(0)
    cnt = 1
    for i in days:
        if sta < i:
            ans.append(cnt)
            sta = i
            cnt = 1
        else:
            cnt += 1
    ans.append(cnt)

    return ans


# 3. 올바른 괄호
def solution3(s):
    stack = []
    for i in s:
        if i == '(':
            stack.append(i)
        else:
            if stack:
                stack.pop()
            else:
                return False

    return False if stack else True

# 4. 프로세스
def solution4(priorities, location):
    # 1. 프로세스 만들기
    queue = []
    for idx ,ele in enumerate(priorities):
        queue.append((ele ,idx))
    # 2. 우선 순위 젤 높은거 뽑기 위해서
    priorities.sort()
    maxi = priorities.pop()
    # 3. 프로세스 처리하기
    cnt = 0
    while True:
        process = queue.pop(0)
        if process[0] == maxi:
            cnt += 1
            if process[1] == location:
                break
            maxi = priorities.pop()
        else:
            queue.append(process)

    return cnt


# 5. 다리를 지나는 트럭
def solution5(bridge_length, weight, truck_weights):

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

# 6. 주식가격
def solution(prices):
    answer = [0] * len(prices)
    for idx, ele in enumerate(prices):

        check = False

        for k in range(idx + 1, len(prices)):
            if ele > prices[k]:
                check = True
                answer[idx] = k - idx
                break

        if check == False:
            answer[idx] = len(prices) - idx - 1

    return answer


def solution6(prices):
    ans = []
    idx = -1
    while prices:
        standard = prices.pop(0)
        idx += 1
        time = 1
        for i in prices:
            time += 1
            if standard > i:
                ans.append(time)