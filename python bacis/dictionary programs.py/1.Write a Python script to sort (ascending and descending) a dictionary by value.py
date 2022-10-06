# Python | Sort Python Dictionaries by Key or Value
"""
a = {
    "key2":"value1",
    "key1":"value4",
    "key4":"value2",
    "key3":"value3"
    }   

print("sorted by items :",sorted(a.items()))
print("sorted by values :",sorted(a.values()))
print("sorted by keys :",sorted(a.keys()))
"""
#------------------------------------------------------------#
# sorted by values based 
key_value = {'ravi': 10, 'rajnish': 9,
		'sanjeev': 15, 'yash': 2, 'suraj': 32}

newDic = {}

# separate the key and value in list 
key = list(key_value.keys())
value = list(key_value.items())

# reverse the items in one by one and store the newDic(variable)
for i in range(len(value)):
    newDic[value[i][1]]=value[i][0]

# here ,sort for reversed items    
s=sorted(newDic.items())

sort = {}
# change back the reversed sorted items

for i in range(len(newDic)):
    sort[s[i][1]]=s[i][0]
# then print the items  
  
print(sort)
#----------------------------------------------------------------#
# another method 
print(sorted(key_value.items(),key=lambda v : v[1]))


# dict = {'ravi': 10, 'rajnish': 9,
#         'sanjeev': 15, 'yash': 2, 'suraj': 32}

# key = list(dict.keys())
# value = list(sorted(dict.values()))         
# di = {}
# for i in range(len(dict.keys())):
#     di[key[i]]=value[i]
# print(di)
