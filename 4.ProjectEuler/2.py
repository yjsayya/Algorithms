a1 = 1
a2 = 2
se = set()

while a1 <= 4_000_000:
    a3 = a1
    a1 = a2
    a2 = a3+a1

    if a2 % 2 == 0:
        se.add(a2)

print(sum(se) + 2)