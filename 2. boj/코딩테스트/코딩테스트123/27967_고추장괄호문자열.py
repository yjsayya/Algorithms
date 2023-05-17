

n = int(input())
s = input()

stack = []
num = 0

for i in s:
    if i == 'G':
        stack.append(i)
    elif i == '(':
        stack.append(i)
        num += 1
    else:
        stack.pop()