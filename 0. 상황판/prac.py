from collections import Counter
li = [1,1,1,1,1,1,2,2,2,3,3,5,5,5,5,5,5,55,6,6,4,7,8,9,9,76,4,3,2,2,2,33,4,5]

counter = Counter(li)
a = sorted(counter.items(), key= lambda x : (-x[1], x[0]))
print(counter.items())
print(a)
print(a[0][0])