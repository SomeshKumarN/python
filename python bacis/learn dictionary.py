data = {
    "key1":"value1",
    "key2":"value2",
    "key3":"value3"
}
# Normal dictionary items now prints  
print(data)
# Indexing by keys
print(data["key1"])
# print only keys
print(data.keys())
# print only values
print(data.values())
# update items
data.update({'key4':'value4','key5':'value5','key6':'value6'})
print("updateitems :",data)
# change value
data.update({'key1':'value2.2'})
print("Change values 2.2 :",data)
data['key1']='value2.3'
print("Change values 2.3 :",data)
data["key7"]='value7'
print('2.4',data)
# copy items
copy= data.copy()
print("copy :",copy)
# delete item
print(data.popitem())
print(data)
data.pop("key1")
print(data)
# set defalt 
data.setdefault("key6","value7")
print('setdefalut',data)
data.update({'key8':None})
data['key8']='value8'
print(data)


abc = ['a', 'b', 'c', 'd', 'e']
num = ["one","two","three"]
a = dict.fromkeys(abc,num)
print(a)
num.append("four")
print(a)

a = {i: i+i for i in range(1,6)}
print(a)

#item price in dollars
old_price = {'milk': 1.02, 'coffee': 2.5, 'bread': 2.5}
mul = 3
new = {k:v*mul for k,v in old_price.items()}
print(new)

original_dict = {'jack': 38, 'michael': 48, 'guido': 57, 'john': 33}

new = {k: v for k,v in original_dict.items() if v < 40}
print(new)

age = {k: "old" if v > 40 else "young" for k,v in original_dict.items()}
print(age)


keys = ['k1','k2','k3','k4']
dic = {
    k1: {k2: k1 for k2  in range(1,11)} for k1 in keys
}
print(dic)