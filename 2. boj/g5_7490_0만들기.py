''''''
"""
    <제한조건>
    - 자연수 n의 범위가 (3 <= n <= 9)라서 완전 탐색으로 접근 가능
    - 수의 리스트와 연산자 리스트를 분리하여 모든 경우의 수를 계산하면 된다 
    
    - python : eval() 내장함수 이럴때 잘 이용하면 된다 ㅋㅋ 
"""

# 재귀함수 만들기
import copy
def solve(array,n):
    # 1. 종료 조건
    if len(array) == n:
        operators_list.append(copy.deepcopy(array))
        return

    array.append(' ')
    solve(array,n)
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
    solve([], n-1)

    integers = [i for i in range(1,n+1)]

    for op in operators_list:
        string = ''
        for i in range(n-1):
            string += str(integers[i]) + op[i]
        string += str(integers[-1])
        if eval(string.replace(" ", "")) == 0:
            print(string)
        print()

    # 2. 문제에 대한 정의


testCase = int(input())
for _ in range(testCase):
    n = int(input())

