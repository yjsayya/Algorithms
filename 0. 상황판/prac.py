''''''
"""
    ** 재귀 함수
    
    1. 종료 조건
    2. 문제에 대한 정의
"""

# 1. 피보나치 수열
def fibo(n): # 0,1,1,2,3 - 5,8,13,21,34 - 55,89 ...
    # 1. 종료 조건
    if n == 1:
        return 0
    elif n == 2:
        return 1
    # 2. 문제에 대한 정확한 정의 : 앞의 두항의 합
    else:
        return fibo(n-1) + fibo(n-2)
print("=== 피보나치 수열 =========")
print(fibo(3)) #1
print(fibo(6)) #5
print(fibo(10)) #34
print(fibo(12)) #89
print("=======================\n")

# 2. 하노이탑
def move_disk(disk_num,start_peg,end_peg):
    print("%d번 원판을 %d번 기둥에서 %d번 기둥으로 이동" %(disk_num, start_peg,end_peg))
def hanoi(num_disk,start_peg,end_peg):
    hanoi_sub(num_disk,start_peg,end_peg,2)
def hanoi_sub(n,start_peg,end_peg,other_peg):
    # 1. 종료 조건 - 시작기둥에서 끝 기둥으로 하나 옮기고 끝내라
    if n == 1:
        move_disk(1,start_peg,end_peg)
    # 2. 문제 정의 : n개의 원반을 ㅇ롬기기 위해서는 n-1원반을 이웃한 기둥으로 옮겨야 합니다.
    else:
        hanoi_sub(n-1,start_peg,other_peg,end_peg)
        move_disk(n,start_peg,end_peg)
        hanoi_sub(n-1,other_peg,end_peg,start_peg)

print("=== 하노이 탑 ============")
print(hanoi(4,1,3))
print("=======================\n")


# boj 1074 - z
# import sys
# N,r,c = map(int,sys.stdin.readline().split())
#

# print("=== z =================")
# print("=======================\n")


import copy


def solve(array, n):  # array 배열, n -
    # 1. 종료조건
    if len(array) == n:
        operators_list.append(copy.deepcopy(array))
        return
    # 2. 문제에 대한 정의
    array.append(' ')
    solve(array, n)
    array.pop()

    array.append('+')
    solve(array, n)
    array.pop()

    array.append('-')
    solve(array, n)
    array.pop()


testCases = int(input())

for _ in range(testCases):
    operators_list = []

    n = int(input())
    solve([],n-1)

    # numList = [i for i in range(1,n+1)]
    #
    # for op in operators_list:
    #     string = ''
    #     for i in range(n-1):
    #         string += str(numList[i] + op[i])
