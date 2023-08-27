

a,p = map(int,input().split())

def seq(x):
    ans = 0
    for i in str(x):
        ans += int(i)**p
    return ans


dic = {a : 1}
while dic[a] != 3:
    a = seq(a)
    if a in dic:
        dic[a] += 1
    else:
        dic[a] = 1

res = []
for j in dic:
    if dic[j] == 1:
        res.append(j)

print(len(res))