


for i in range(1,11):
    print(i)


A = [1,2,3,4,5,6]
B = [2,3,4,5,6,7]

for a,b in zip(A,B):
    print(a*b)

C = [[1,2], [2,3], [3,4]]

for i,j in C:
    print(i + j)

D = [1,2,3,4,5,6,7,8]

for idx, ele in enumerate(D):
    print(idx, ele)