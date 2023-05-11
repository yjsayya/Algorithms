
n = int(input())
pl = []
mi = []
zorone = []

answer = 0

for i in range(n):
    num = int(input())
    if num >= 2:
        pl.append(num)
    elif num < 0:
        mi.append(num)
    elif num == 0 or num == 1:
        zorone.append(num)

while 1 in zorone:
    answer += 1
    zorone.remove(1)

pl.sort()
mi.sort()

# 양수 처리
if len(pl) == 0:
    pass
elif len(pl) == 1:
    answer += pl[0]
elif len(pl) % 2 == 0:
    for i in pl:
        first = pl.pop()
        second = pl.pop()
        answer += first * second
else:
    for k in pl:
        first = pl.pop()
        second = pl.pop()
        answer += first * second
        if len(pl) == 1:
            break

# 음수 처리
if 0 in zorone:
    if len(mi) == 0:
        pass
    elif len(mi) == 1:
        pass
    elif len(mi) % 2 == 1:
        for i in mi:
            first = mi.pop(0)
            second = mi.pop(0)
            answer += first * second
            if len(mi) == 1:
                break
    else:
        for k in mi:
            first = mi.pop(0)
            second = mi.pop(0)
            answer += first * second
else:
    if len(mi) == 0:
        pass
    elif len(mi) == 1:
        answer += mi[0]
    elif len(mi) % 2 == 1:
        while len(mi) > 2:
            first = mi.pop(0)
            second = mi.pop(0)
            answer += first * second
    else:
        for k in mi:
            first = mi.pop(0)
            second = mi.pop(0)
            answer += first * second

        answer += mi[0]

print(answer)