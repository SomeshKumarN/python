#def function(a,b):
#    return a+b
#print(function(a='somnath',b='vishnu'))

def class_10(*students):
    print(students)
    for user in students:
        print(user)
        print(type(user))
 
 
class_10(7, "Sam", "Raja", "Sara")

def message(name, age):
    print(name, " age is ", age)
 
 
message(age=25, name="Ram")

def bioData(**data):
    print(data)
 
 
bioData(name="Ram Kumar", age=25, gender="Male")
 