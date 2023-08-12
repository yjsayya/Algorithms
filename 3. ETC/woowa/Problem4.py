""""""
"""

"""

def solution(word):
    abc = list('abcdefghijklmnopqrstuvwzyz')
    alphabetDic = dict()
    for i,j in zip(abc,sorted(abc,reverse=True)):
        alphabetDic[i] = j

    ans = ''
    for w in word:
        if w.isalpha() and w.isupper():
            ans += alphabetDic[w.lower()].upper()
        elif w.isalpha() and w.islower():
            ans += alphabetDic[w]
        elif w == ' ':
            ans += ' '

    return ans


print(solution("I love You"))


