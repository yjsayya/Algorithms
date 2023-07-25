
# boj 5397
testcase = int(input())

for _ in range(testcase):
    inputWord = input()

    stack1 = []
    stack2 = []

    for word in inputWord:
        if word == '<':
            if stack1:
                stack2.append(stack1.pop())
        elif word == '>':
            if stack2:
                stack1.append(stack2.pop())
        elif word == '-':
            if stack1:
                stack1.pop()
        else:
            stack1.append(word)

    stack2.reverse()
    print("".join(stack1) + "".join(stack2))