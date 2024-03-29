

"""
DP로 풀어야하는 문제네 --> 이거 꼭 다시 복습해보자!!
"""
def solution(n):
    if n <= 2:
        return 1

    dp = [0] * (n + 1)
    dp[0] = dp[1] = 1

    for i in range(2, n + 1):
        for j in range(1, i + 1):
            dp[i] += dp[j - 1] * dp[i - j]

    return dp[n-1] % 10007