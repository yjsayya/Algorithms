# import sys, heapq
#
# # 1. 입력 받기
# n = int(input())
# li = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
#
# # 2. 정렬해줌
# li.sort()
#
# # 3. heapq로 정렬
# queue = []
# heapq.heappush(queue, li[0][1])
#
# for i in range(1,n):
#     if li[i][0] < queue[0]:
#         heapq.heappush(queue, li[i][1])
#     else:
#         heapq.heappop(queue)
#         heapq.heappush(queue, li[i][1])
#
# print(len(queue))


# import sys,heapq
#
# n = int(sys.stdin.readline())
# li = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
#
# li.sort(key= lambda x : x[0])
#
# q = []
# heapq.heappush(q, li[0][1])
#
# for i in range(1,n):
#     if li[i][0] < q[0]:
#         heapq.heappush(q,li[i][1])
#     else:
#         heapq.heappop(q)
#         heapq.heappush(q,li[i][1])
#
# print(len(q))

# import heapq
# def solution(book_time):
#     cnt = 0
#     hq = []
#     heapq.heapify(hq)
#
#     # 1. 정렬하기
#     book_time.sort(key=lambda x : (x[0][:2], x[0][3:]))
#
#     # 2. heapq에 값 넣기
#     heapq.heappush(hq,int())
#
#
#
# print(solution([["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]]))
#
# def plusTenMin(hr,min):
#     if 0 <= min <= 49:
#         return str(hr) + ':' + str(min+10)
#     else:
#         strMin = '0' + str((min+10) % 60)
#         if hr == 23:
#             return '00:' + strMin
#         else:
#             return str(hr+1) + ':' + strMin
