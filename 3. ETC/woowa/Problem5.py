""""""
"""
    동전 수 세기 
    전형적인 그리디 문제였지 -- 어렵지 않게 바로 풀어버렸다 
"""

def solution(money):
    coins = [50_000,10_000,5_000,1_000,500,100,50,10,1]

    ans = []
    for coin in coins:
        ans.append(money // coin)
        money %= coin

    return ans

print(solution(50_237))
print(solution(15_000))
