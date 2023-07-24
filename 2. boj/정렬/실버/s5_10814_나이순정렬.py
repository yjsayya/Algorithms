a = '실버 5'
"""
    - python의 sort() or sorted()는 바로 사전순으로 정렬해주지는 않는다
        **정렬 기준으로 정렬하되 그 외의 것들은 넣은 순서 그대로 정렬이 된다
    
    - int() 꼭 넣어줬야 했는데 ㄲㅂ
    - 12에 대한 정렬과 '12'에 대한 정렬이 분명 다르다는 것도 꼭 알아두자
"""

import sys

n = int(sys.stdin.readline())
li = []

for i in range(n):
    a,b = sys.stdin.readline().split()
    li.append([int(a),b])

for k in sorted(li, key= lambda x : x[0]):
    print(f"""{k[0]} {k[1]}""")