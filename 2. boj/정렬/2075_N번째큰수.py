'''
    제한사항 
    - n(1 ≤ n ≤ 1,500)
    - -10억 ~ 10억 사이의 정수
'''
# import sys 
# # sys.stdin.readline().split()
# n = int(input())
# matrix = []

# for _ in range(n):
#     matrix.append(list(map(int, sys.stdin.readline().split())))

# # count
# answer = max(matrix[n-1])
# y,x = n-1, matrix[y].index(answer)

# for _ in range(n):
#     if matrix[y-1][x] > max():


# def check(matrix, x, y):



import sys, heapq

n = int(input())
q = []
for i in range(n):
	num_list = list(map(int, sys.stdin.readline().split()))
	if not q: # q에 아무것도 없는 첫번째 입력 시
		for num in num_list:
			heapq.heappush(q, num) # min_heap 구조로 q 채우기
	else:
		for num in num_list: # q에 값이 있을 시 늘 q의 길이를 n으로 유지하기
			if q[0] < num: # q 최솟값보다 현재 숫자가 클 경우 n번째로 큰 수가 바뀌어야 하기 때문에
				heapq.heappush(q, num) # 현재 숫자를 push 하고
				heapq.heappop(q) # 기존 최솟값 pop
print(q[0])