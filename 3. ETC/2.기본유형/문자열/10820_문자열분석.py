# 시간복잡도 --> O(100 * 100)

# 첫번째로 푼 풀이
import sys

while True:
    s = sys.stdin.readline().rstrip('\n')

    if not s:
        break

    for _ in range(10):
        strings = input()
        upp, low, num = 0, 0, 0
        space = strings.count(' ')
        for k in strings:
            if k.isupper():
                upp += 1
            elif k.islower():
                low += 1
            elif k.isdigit():
                num += 1
        print(low, upp, num, space)

# 소문자, 대문자, 숫자, 공백의 개수
