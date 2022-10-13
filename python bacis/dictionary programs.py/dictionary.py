data = {
    'name':'somnath',
    'age':25,
    'address':'mahilankottai',
    'age':25
}
print(data)
print(type(data))
print(data['name'])
print("age is :",data['age'])
print(data.get('address'))
print(data.keys())
print(data.values())
print(data.items())

#access in for loop:

for i in data:
    print(i,':',data[i])
for i in data.values():
    print(i)
for i in data.keys():
    print(i)
for i,x in data.items():
    print(i,':',x) 

# # checking in keys:

# if 'age' in data:
#     print('yes') 

# #checking in values:

# if 25 in data.keys():
#     print('present')

# # keys cannot be changed
# # update values

# data.update({'gender':'male'})
# print(data)

