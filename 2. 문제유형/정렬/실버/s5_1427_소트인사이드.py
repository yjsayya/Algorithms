a = "실버 5"
"""
    실버 5 정도는 문제 없이 풀 수 있다 
"""

n = input()
li = []

for i in n:
    li.append(i)

li.sort(reverse=True)
print(int("".join(li)))


# python틱하게 푸려면 -- 이렇게 풀도록 하자
numList = list(input())
print("".join(sorted(numList, reverse=True)))