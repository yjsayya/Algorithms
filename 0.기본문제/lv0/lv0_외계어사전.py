# 졸라 지저분하게 푼 첫번재 풀이
def solution(spell, dic):
    answer = 2

    for i in dic:
        if len(i) != len(spell):
            dic.remove(i)

    if len(dic) != 0:
        for j in dic:
            cnt = 0
            for k in spell:
                if k not in j:
                    break
                else:
                    cnt += 1

            if cnt == len(spell):
                answer = 1
                break
    return answer