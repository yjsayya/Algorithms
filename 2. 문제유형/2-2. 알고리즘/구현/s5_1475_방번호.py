""""""

"""
    6,9만 처리하면 된다     
"""

n = input()
dic = {i: n.count(i) for i in n}
# 6,9 숫자 따로 처리
if '6' not in dic and '9' not in dic:
    pass
elif '6' not in dic:
    dic['9'] = (dic['9'] + 1) // 2
elif '9' not in dic:
    dic['6'] = (dic['6'] + 1) // 2
else:
    mini = min(dic['6'], dic['9'])
    dic['69'] = mini + (max(dic['9'] - mini, dic['6'] - mini) + 1) // 2
    del dic['6']
    del dic['9']

print(sorted(dic.items(), key=lambda x: -x[1])[0][1])