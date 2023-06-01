
'''
    정렬 문제 
    - 아오 귀찮아 ~
'''


# 입학연도 % 100 - 오름차순으로 정렬해서 이어붙인 문자열

import sys

li1 = sys.stdin.readline().rstrip().split()
li1[0] = int(li1[0])
li1[1] = int(li1[1])

li2 = sys.stdin.readline().rstrip().split()
li2[0] = int(li2[0])
li2[1] = int(li2[1])

li3 = sys.stdin.readline().rstrip().split()
li3[0] = int(li3[0])
li3[1] = int(li3[1])

# 1. 1st 가이드라인
firstGL = []
a = [li1[1]%100, li2[1]%100, li3[1]%100]
for i in a:
    firstGL.append(str(i))

# 2. 2nd 가이드라인
secondGL = dict()

secondGL[li1[2]] = li1[0]
secondGL[li2[2]] = li2[0]
secondGL[li3[2]] = li3[0]

a = ""

for i in sorted(secondGL.keys(), key=lambda x : -secondGL[x]):
    a += i[0]

print("".join(sorted(firstGL)))
print(a)