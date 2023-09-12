

three = 0
five = 0
for i in range(3,1000):
    if i % 3 == 0:
        three += i
    elif i % 5 == 0:
        five += i

print(three + five)