def solution(n):
    # 1. 삼각 달팽이 좌표 만들기
    matrix = [[0]*n for _ in range(n)]
    x,y,num = -1,0,1
    for i in range(n):
        for j in range(i,n):
            if i % 3 == 0:
                x += 1
            elif i % 3 == 1:
                y += 1
            else:
                x -= 1
                y -= 1
            matrix[x][y] = num
            num += 1
    # 2. ans 배열에 넣고 return 하기
    idx = 0
    ans = list()
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 0:
                break
            ans[idx] = matrix[i][j]
            idx += 1

    return ans


def solution(n):
    # 1. 삼각 달팽이 좌표 만들기
    matrix = [[0] * n for _ in range(n)]
    x, y, num = -1, 0, 1
    for i in range(n):
        for j in range(i, n):
            if i % 3 == 0:
                x += 1
            elif i % 3 == 1:
                y += 1
            else:
                x -= 1
                y -= 1
            matrix[x][y] = num
            num += 1
    # 2. ans 배열에 넣고 return 하기
    ans = list()
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 0:
                break
            ans.append(matrix[i][j])

    return ans