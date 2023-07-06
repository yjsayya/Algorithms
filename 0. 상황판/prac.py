# import heapq
#
# def solution(book_time):
#     book_time.sort()
#
#     q = []
#     heapq.heappush(q, book_time[0][1])
#
#     for i in range(1, len(book_time)):
#         a, b = map(int, q[0].split(':'))
#         qe = ''
#         if b < 50:
#             qe = str(a) + ':' + str(b + 10)
#         else:
#             if a == 23:
#                 qe = '00:' + '0' + str((b + 10) % 60)
#             elif 0 <= a < 9:
#                 qe = '0' + str(a + 1) + ':' + '0' + str((b + 10) % 60)
#             else:
#                 qe = str(a + 1) + ':' + '0' + str((b + 10) % 60)
#
#         if book_time[i][0] < qe:
#             heapq.heappush(q, book_time[i][1])
#         else:
#             heapq.heappop(q)
#             heapq.heappush(q, book_time[i][1])
#
#     return len(q)
#
#
# print(solution([["10:10", "12:50"], ["10:20", "12:30"], ["10:20", "12:30"]]))
import heapq

q = []

heapq.heappush(q,4)
heapq.heappush(q,1)
heapq.heappush(q,6)
heapq.heappush(q,2)
heapq.heappush(q,7)
heapq.heappush(q,3)

print(q)
