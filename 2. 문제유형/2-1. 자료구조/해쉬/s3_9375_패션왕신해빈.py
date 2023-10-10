""""""
"""

"""

import sys

def get_ans(n):
    dic = dict()
    for _ in range(n):
        name, clothes = sys.stdin.readline().split()
        if clothes in dic:
            dic[clothes].append(name)
        else:
            dic[clothes] = [name]

    ans = 1
    for i in dic:
        ans *= len(dic[i])+1

    return ans -1


test_case = int(sys.stdin.readline().strip())

for _ in range(test_case):
    n = int(sys.stdin.readline().rstrip())
    print(get_ans(n))