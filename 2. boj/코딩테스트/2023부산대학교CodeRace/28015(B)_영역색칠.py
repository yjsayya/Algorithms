import sys

n, m = map(int, sys.stdin.readline().split())
cnt = 0

for _ in range(n):

    li = list(map(int,sys.stdin.readline().split()))

    # 전부 0이 될때까지 진행 
    while sum(li) > 0:
        li.append(0)
        for i in range(1, len(li)):
            if li[i-1] != 0 and li[i] == 0:
                cnt += 1
                li[i-1] -= 1
            elif li[i-1] != 0 and li[i] != 0:
                li[i-1] -= 1
        li.pop()

print(cnt)



# def solution(li):
#     cnt = 0
    
#     while sum(li) != 0:
#         li.append(0)
#         for i in range(1, len(li)):
#             if li[i-1] != 0:
#                 if li[i] == 0:
#                     li[i-1] -= 1 
#                     cnt += 1
#                 else:
#                     li[i-1] -= 1
#         li.pop()
#     return cnt

# print(solution([1,1,0,0]))
# print(solution([2,2,0,1]))