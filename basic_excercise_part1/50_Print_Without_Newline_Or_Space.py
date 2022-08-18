"""Write a Python program to print without newline or space."""

#Solution:

givenStr = "Hi, How are you?\nHad your lunch?\nWe will meet tomorrow.\n"
print("Given String:\n",givenStr)
givenStr = givenStr.replace("\n","").replace(" ","")
print("After formating newline and space:\n",givenStr)