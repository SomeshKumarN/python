"""Write a Python program to test whether a passed letter is a vowel or not."""

#Solution:

test=1

def isVowel(inp:str):
    global test
    print("\nTest-->",test)
    try:
        if (1<inp.__len__()<2 and inp in ['a','e','i','o','u']):
            print("Given char-'",inp,"' is vowel")
        else:
            print("Given char-'",inp,"' is consonent")
    except:
        print("Please enter only char value")
    test+=1


#Test
isVowel(4)
isVowel('a')
isVowel('s')
isVowel(5)
isVowel(True)
isVowel("som")