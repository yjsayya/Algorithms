# 세자리 수를 곱해 만들 수 있는 가장 큰 대칭 수

se = set()

for i in range(100,1000):
    for j in range(i,1000):
        a = str(i*j)
        if len(str(a)) == 5:
            if a[0] == a[4] and a[1] == a[3]:
                se.add(int(a))
        else:
            if a[0] == a[5] and a[1] == a[4] and a[2] == a[3]:
                se.add(int(a))

print(max(se))