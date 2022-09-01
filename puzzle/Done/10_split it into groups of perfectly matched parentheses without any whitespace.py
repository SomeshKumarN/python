"""
Given a string consisting of whitespace and groups of matched parentheses, 
write a Python program to split it into groups of perfectly matched parentheses without any whitespace.
Input:( ()) ((()()())) (()) ()
Output:
['(())', '((()()()))', '(())', '()']
Input:
() (( ( )() ( )) ) ( ())
Output:
['()', '((()()()))', '(())']

step 1 : take the string
step 2 : change white space to non white space
step 3 : iterate the brackets by one by one
step 4 : while iterate check open bracket and close brackets are equal
step 5 : store any location until the brackets are equal
step 6 : if the brackets are equal return list
step 7 : if the brackets are not equal return list

"""

def a(brackets):
    lst = []
    remove_s = brackets.replace(' ','')
    brackets_2 = ''
    for i in remove_s:
        brackets_2 = brackets_2 + i
        if brackets_2.count('(') == brackets_2.count(')'):
            lst.append(brackets_2)
            brackets_2 = ''
    print(lst)    
a("( ()) ((()()())) (()) ()")
a('() (( ( )() ( )) ) ( ())')
a("(()))")