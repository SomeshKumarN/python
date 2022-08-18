# Write a Python program to test whether a passed letter is a vowel or not.


def compare(a):
    #a = input("Enter a letter :")
    b = "a, e, i, o, u"
    for i in b:
        if a == i:
            print(i)
    else:
        print("Given letter is not vowel")
compare('a')
compare('c')
compare('ad')
compare(3)
compare('')
compare(True)






