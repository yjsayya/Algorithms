"""
global vs nonlocal

<< 변수의 범위 총정리 >>
    - 범위라는 것은 ㅈㄴ 상대적
    - var1, var2, var3가 있다고 할 때;
    --> 바깥 쪽 범위 내에서 선언된 변수를 안 쪽 범위에서는 접근할 수 있지만 
        (var1을 outer()함수와 inner()함수는 접근하고 사용할 수 있다)
    --> 그 반대는 불가능하다
        (outer()함수 내에 정의된 var2는 바깥에서 접근할 수가 없다) 
        (inner()함수 내에 정의된 var3는 outer()함수에서 접근할 수가 없다) 
        
"""


# var1 = 1
#
# def outer():
#     var2 = 1
#     def inner():
#         var3 = 1
#         return var3
#
# # 예시 1 - global
# num = 100
# def method():
#     global num
#     num = 200
#     print(num)
#
# print(num)
# method()

# import sys
#
# string = sys.stdin.readline().rstrip()
# n = int(sys.stdin.readline().rstrip())
# li = []
#
# for _ in range(n):
#     word = sys.stdin.readline().rstrip().split()
#     li.append([word[0],int(word[1])])
#
# li.sort(key=lambda x : -x[1])
#
# ans = 0
# for i in li:
#     while i[0] in string:
#         string = string.replace(i[0], '_'*len(i[0]),1)
#         ans += i[1]
#
# print(ans + len(string) - string.count('_'))




# 우테코 1주차 - 7번 문제

def solution(n):
    # 1. 자릿수 먼저 구하기
    idx = 0
    for i in range(1,n+1):
        sn = 3*(3**i-1)//2
        if sn == n:
            return '4' * i
        elif sn > n:
            idx = i
            break
    # 2. 해당 자리에서 몇번째 인가?
    cnt = n - (3*(3**(idx-1) -1)//2)

    # 3. 이제 구하자




# 1-3 : 한자리
# 4-12 : 두자리
# 13 - 40: 세자리

print(solution(14))
print(solution(15))
print(solution(38))
print(solution(39))




# 3, 9 27 81

# 1,2,4
#
# 11,12,14
# 21 22 24
# 41 42 44

# 111 112 114
# 121 122 124
# 141 142 144

# 211 212 214
# 221 222 224
# 241 242 244

# 411 412 414
# 421 422 424
# 441 442 444