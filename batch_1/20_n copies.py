i = input("Enter string :")
try:
    n = int(input("Enter how many copies :"))
    print("string copies :", i*n)
except ValueError:
    print("Error :Please Enter The Integer Value ")


