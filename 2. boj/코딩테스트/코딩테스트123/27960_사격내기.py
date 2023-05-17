
trg = [512,256,128,64,32,16,8,4,2,1]

li = list(map(int,input().split()))
a = li[0]
b = li[1]

a_trg = []
b_trg = []

for i in trg:
    if a >= i:
        a -= i
        a_trg.append(i)
    
for j in trg:
    if b >= j:
        b -= j
        b_trg.append(j)
    
print(sum(set(a_trg) - set(b_trg)) + sum(set(b_trg) - set(a_trg)))