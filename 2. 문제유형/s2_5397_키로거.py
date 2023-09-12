a = 100
"""
    ** 아이디어 - 이중 스택 구조를 이용하여 푸는 문제
    left_stack '커서' right_stack
    - 마지막에 right_stack은 뒤집어야 한다는 것까지 알면 된다 !!!
"""

testCases = int(input())

for _ in range(testCases):
    inputWord = input()
    left = []
    right = []

    for word in inputWord:
        if word == '-':
            if left:
                left.pop()
        elif word == '<':
            if left:
                right.append(left.pop())
        elif word == '>':
            if right:
                left.append(right.pop())
        else:
            left.append(word)

    left.extend(reversed(right))
    print(''.join(left))