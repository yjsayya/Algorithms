li = [1,2,3,4,5,6,7]
se = {2,3,4,5,6,7}

string1 = '0123456789'
string2 = 'abcdefghijklmnopqrs'


dic = dict()

data = {
    'apple': 3,
    'banana': 1,
    'cherry': 2
}

data_dic = sorted(data.keys(), key=lambda x : data[x])
data_dic_values = sorted(data.values(), reverse=True)

data_dic_items = sorted(data.items(), key=lambda x : x[1])


print(data_dic)
print(data_dic_values)
print(data_dic_items)
