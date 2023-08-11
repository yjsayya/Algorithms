def solution(user, friends, visitors):
    friendScore = dict()
    # 1. dic 만들기
    dic = dict()
    for i, j in friends:
        if i in dic:
            dic[i].append(j)
        else:
            dic[i] = [j]

        if j in dic:
            dic[j].append(i)
        else:
            dic[j] = [i]

    # 2. 함께 아는 친구의 수 - 구하기
    userSet = set(dic[user])
    dic.pop(user)
    for i in dic:
        friendScore[i] = len(set(dic[i]) & userSet) * 10

    # 3. 방문자 점수 - 구하기
    for i in visitors:
        if i not in friendScore:
            friendScore[i] = visitors.count(i)

    ans = sorted(friendScore.keys(), key=lambda x : (-friendScore[x], x))[:5]

    for _ in range(len(ans)):
        if friendScore[ans[-1]] == 0:
            ans.pop()
        else:
            break

    return ans



print(solution("mrko",
               [["donut", "andole"], ["donut", "jun"], ["donut", "mrko"], ["shakevan", "andole"], ["shakevan", "jun"],["shakevan", "mrko"]],
               ["bedi", "bedi", "donut", "bedi", "shakevan"]))
