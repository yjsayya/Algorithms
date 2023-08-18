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
