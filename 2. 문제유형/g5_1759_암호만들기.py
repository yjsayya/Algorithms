""""""
"""

"""

from itertools import combinations as comb
import sys

l, c = map(int,sys.stdin.readline().split())
abc = list(sys.stdin.readline().split())

vowel = ['a','e','i','o','u']

abc_vowel = []
abc_consonant = []
# 알파벳 분류
for i in abc:
    if i in vowel:
        abc_vowel.append(i)
    else:
        abc_consonant.append(i)

# 정답 뿌리기
ans = []
for k in range(1,len(abc_vowel)+1):
    for i in list(comb(abc_vowel,k)):
        for j in list(comb(abc_consonant,l-k)):
            if l-k < 2:
                break
            code = "".join(i) + "".join(j)
            ans.append("".join(sorted(code)))

for i in sorted(ans):
    print(i)

# 4,