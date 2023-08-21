""""""
"""

"""

def solution(menu,order,k):
    ans = []
    mkList = [menu[order[0]]]

    idx = 1
    while True:
        for i in range(len(mkList)):
            time = k
            if mkList[i] > time:
                mkList[i] -= time
                break
            else:
                mkList[i] = 0
                time -= mkList[i]

        while mkList and mkList[0] == 0:
            mkList.pop(0)

        mkList.append(menu[order[idx]])

        ans.append(len(mkList))
        idx += 1
        if idx == len(order):
            break

    return max(ans)


from collections import deque

def solution2(menu,order,k):
    ans = 0
    n = len(order)
    dq = deque()
    i = 0
    time = 0

    while dq or i < n:
        if not dq:
            time = i*k + menu[order[i]]
            i += 1
        else:
            x = dq.popleft()
            time += menu[x]

        while i < n and i <= ((time-1)//k):
            dq.append(order[i])
            i += 1
        ans = max(ans, len(dq))

    return ans + 1