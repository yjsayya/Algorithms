


li = [1,2,3,4,5]

import copy

a = copy.deepcopy(li)
a.pop()

print(a)
print(li)