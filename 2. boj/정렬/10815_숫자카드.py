'''
    제한사항 
    - n(1 ≤ n ≤ 500,000)
    - m(1 ≤ m ≤ 500,000)

    ** 시간 복잡도 꼭 고려 해줘야한다
    
    확실히, li로 푸는 것보다는 set으로 풀어야 시간복잡도가 좋다!!
'''
import sys

n = int(input())
card = set(map(int, sys.stdin.readline().split()))
m = int(input())
check = list(map(int, sys.stdin.readline().split()))

for i in check:
    card.add(i)
    if n - len(card) == 0:
        print(1, end=" ")
    else:
        card.discard(i)
        print(0, end=" ")