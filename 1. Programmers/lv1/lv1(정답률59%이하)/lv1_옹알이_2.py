""""""
"""
    깊은 복사와 얕은 복사에 대한 개념 잘 이해해둘 것
    - 일반 변수는 신경 안 써도 됨
    - 자료형 변수들은 신경 써줘야 함 
"""


def solution(babbling):
    dic = {
        "aya": "1",
        "ye": "2",
        "woo": "3",
        "ma": "4",
    }
    new_babbling = []
    for word in babbling:
        for i in dic:
            if i in word:
                word = word.replace(i, dic[i])
        new_babbling.append(word)

    cnt = 0
    for w in new_babbling:
        if w.isdigit() and len(w) == len(set(w)):
            cnt += 1

    return cnt