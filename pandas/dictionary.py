dic = {
    'key1':1,
    'key2':2,
    'key3':3,
    'key4':4
}

dic.update({'key5':5})
dic['key6'] = 6
# print(dic)

# del dic['key6']
# dic.pop('key5')
# dic.popitem()
# print(dic)

# dic.update({'key1':3})
# dic.setdefault('key3',3)
# dic['key1']=8

# print(dic['key1'])

diction = dic
d = dic.copy()
# print(d)

abc = [1,2,3,4]
com = ['hi','som','name','nath']
di =dict()
# for i in range(len(com)):
di = dict.fromkeys(abc,com)
print(di)
