''''''
"""
    ** 진짜 전혀 감을 잡을 수가 없었다
    
    1. 삼각형 구조 만드는 이중 for문 만드는거 하나 가져가고
    2. 3으로 나누어서 가져가는 아이디어를 가져가자
"""


def solution(n):
    # 1. 삼각형 구조 만들기
    ans = [[0 for _ in range(1,i+1)] for i in range(1,n+1)]
    # 2, 좌표 초기화
    x,y = -1,0
    num = 1
    # 3. for문 돌리기
    for i in range(n): # 방향
        for j in range(i,n):
            if i % 3 == 0:
                x += 1
            elif i % 3 == 1:
                y += 1
            else:
                x -= 1
                y -= 1

            ans[x][y] = num
            num += 1

    return sum(ans,[])