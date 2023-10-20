



# 내가 푼 풀이
def solution1(prices):
    n = len(prices)
    maxi = 0
    for left in range(n):
        for right in range(left+1,n):
            benefit = prices[right]-prices[left]
            if maxi < benefit:
                maxi = benefit
    return maxi


# GPT 에게 손봐달라고 한 풀이
def solution2(prices):
    n = len(prices)
    min_price = prices[0]  # 현재까지의 최소 가격
    max_profit = 0  # 현재까지의 최대 이익

    for i in range(1, n):
        current_price = prices[i]
        if current_price < min_price:
            min_price = current_price
        else:
            profit = current_price - min_price
            if profit > max_profit:
                max_profit = profit

    return max_profit