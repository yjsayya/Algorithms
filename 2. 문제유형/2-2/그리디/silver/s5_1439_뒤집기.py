'''
    s를 처음부터 끝까지 한번만 읽으면 답을 알 수 있는 O(n) 시간복잡도 풀이
    이런건 뭐 스택으로 풀면 깔끔하지 뭐

    ** 스택 마지막 처리하는 것 잊지 말자
'''

s = input()

stack = []
cnt0 = 0
cnt1 = 0

for i in s:
    if len(stack) == 0:
        stack.append(i)
    else:
        if stack[0] == '0' and i == '1':
            stack.pop()
            stack.append(i)
            cnt0 += 1
        elif stack[0] == '1' and i == '0':
            stack.pop()
            stack.append(i)
            cnt1 += 1

if stack[0] == '1': cnt1 += 1
else: cnt0 += 1

print(min(cnt0, cnt1))