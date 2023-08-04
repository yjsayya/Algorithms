def solution(priorities, location):

    process = []
    for idx, ele in enumerate(priorities):
        process.append((ele,idx))

    priorities.sort()

    cnt = 0
    maxi = priorities.pop()
    while True:
        if process[0][0] == maxi:
            maxi = priorities.pop()
            process.pop(0)
            cnt += 1
            if process[0][1] == location:
                break
        else:
            process.append(process.pop(0))

    return cnt

print(solution([2, 1, 3, 2], 2))
print(solution([1,1,9,1,1,1], 0))
