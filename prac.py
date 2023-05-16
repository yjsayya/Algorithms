

dic = dict()

dic[0] = "zero"
dic[1] = "one"
dic[2] = "two"
dic[3] = "three"
dic[4] = "four"
dic[5] = "five"
dic[6] = "six"

print(dic)

print(sorted(dic, key=lambda x : dic[x][1], reverse=True))

