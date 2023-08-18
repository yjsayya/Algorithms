""""""
"""
    역시 1번은 무조건 다 맞아야하는 문제
    절대로 틀리면 안된다!!!
    
    쉬운 구현 문제 --> 예외처리를 잘하면 어렵지 않게 풀 수 있는 문제 였다
"""


# 첫번째 - 내가 푼 풀이
#   공간복잡도가 높아지게 굳이 dir, move를 따로 둘 필요가 없었는데 다소 아쉬운 풀이
#   dir = [(0,1),(1,0),(1,0),(-1,0)]
#   이렇게 두고 푸는 것이 훨씬 나았을 듯 하다
def solution(command):
    dir = ['up', 'right', 'down', 'left']
    move = {
        'up': (0, 1),
        'down': (0, -1),
        'left': (-1, 0),
        'right': (1, 0)
    }

    idx,x,y = 0,0,0

    for i in command:
        if i == 'R':
            idx = (idx+1) % 4
        elif i == 'L':
            idx = (idx-1) % 4
        elif i == 'G':
            x += move[dir[idx]][0]
            y += move[dir[idx]][1]
        elif i == 'B':
            x -= move[dir[idx]][0]
            y -= move[dir[idx]][1]

    return [x, y]


# 다른 사람 풀이 가져왔다 - 깔끔해보여서 가져왔다
def solution1(command):
    path = [[0,1], [1,0], [0,-1], [-1, 0]]
    x = y = d = 0

    for i in command:
        if i == 'R': d = (d+1)%4
        elif i == 'L': d = (d+3)%4
        elif i == 'G':
            x += path[d][0]
            y += path[d][1]
        elif i == 'B':
            x -= path[d][0]
            y -= path[d][1]

    return [x,y]


# 다른 사람풀이
def solution3(command):
    answer = [0, 0]
    direction = 0
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    for c in command:
        if c == 'R':
            direction = (direction + 1) % 4
        elif c == 'L':
            direction = (direction - 1)
            if direction < 0:
                direction += 4
        elif c == 'G':
            answer[0] += dx[direction]
            answer[1] += dy[direction]
        elif c == 'B':
            answer[0] -= dx[direction]
            answer[1] -= dy[direction]

    return answer