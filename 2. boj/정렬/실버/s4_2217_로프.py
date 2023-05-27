'''
    제한사항
    - N(1 ≤ N ≤ 100,000)
    - 줄 하나당 최대 중량은 10,000
    - 모든 로프를 사용해야 할 필요는 없으며, 
        임의로 몇 개의 로프를 골라서 사용해도 된다.

    제한 사항이 크지 않아서 for문 무리 없이 돌렸다
    idea 
        - 정렬하고
        - 작은 수부터 빼면서 견딜 수 있는 하중 값을 모두 구하고
        - 그 중 가장 큰 값을 print 하였다
'''

n = int(input())
li = [int(input()) for _ in range(n)]

li.sort()

answer = [li[idx] * (n-idx) for idx in range(n)]
print(max(answer))