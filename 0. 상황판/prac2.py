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

tc = int(input())

def solv():
    global n,answer
    n = int(input())
    answer = []
    select_operator(2,'1')
    print()
def select_operator(now,ans):
    global answer
    if now == n+1:
        tmp = ans.replace(' ', '')
        if eval(tmp) == 0:
            print(ans)
        return

    select_operator(now+1,ans+' '+str(now))
    select_operator(now+1,ans+'+'+str(now))
    select_operator(now+1,ans+'-'+str(now))

for _ in range(tc):
    solv()

# =================================================================
def operator(now,ans):
    if now == n+1:



testCase = int(input())

for _ in range(testCase):
    n = int(input())
    ans = []

