def solution(arr):
    stack = []
    for i in arr:
        if stack:
            if stack[-1] != i:
                stack.append(i)
        else:
            stack.append(i)

    return stack