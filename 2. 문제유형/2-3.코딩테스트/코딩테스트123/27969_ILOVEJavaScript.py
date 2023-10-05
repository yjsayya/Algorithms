
# 양의 정수 자료형 - 8
# 문자열 - 12 + 문자열의 길이
# 다른 ASON - 

# 첫번째 풀이
    # --> 되게 어려워 보이지만 풀어보면 개 쉬운 문제 였음
import sys
ason = list(sys.stdin.readline().split())
mem = 0

for i in ason:
    if i.isdigit() == True:
        mem += 8
    elif i.isalpha():
        mem += 12 + len(i)
    elif i ==']':
        mem += 8

print(mem)
