""""""
"""
    와 이게 어떻게 이렇게 나오냐 ..?!
"""

import sys

test_case = int(sys.stdin.readline().rstrip())
dp = [0] * 1001
dp[0] = 1
for _ in range(test_case):
    n = int(sys.stdin.readline().rstrip())
    for i in range(1,n+1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    print(dp[n])