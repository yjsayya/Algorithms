def solution(n):
    is_prime = [True] * (n + 1) # 0~n 까지의 수를 모두 소수로 가정
    is_prime[0] = is_prime[1] = False # 0, 1은 소수가 아님

    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False

    return len([x for x in range(2, n + 1) if is_prime[x]])


# '에라토스테네스의 체'를 이용하는 것이 현재 가장 시간복잡도가 빠른 알고리즘 인 듯
# 시간 복잡도 : O(nlog(log n))