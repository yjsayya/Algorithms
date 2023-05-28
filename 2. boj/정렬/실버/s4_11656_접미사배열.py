'''


'''

n = input()
li = [n[i:] for i in range(len(n))]

for i in sorted(li):
    print(i)