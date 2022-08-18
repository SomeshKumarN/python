"""Write a Python program to count the number 4 in a given list."""

#Solution:

test =1

def countElementInList(_list:list,elementToFind:any):
    global test
    print("\nTest--",test)
    print("Given list is--",_list)
    if elementToFind in _list:
        print(_list.count(elementToFind)," times the element ",elementToFind," is present in the list.")
    else:
        print(elementToFind," is not available in the list --", _list)
    test+=1

#Tests
countElementInList([1,2,3,4,2,3,2],2)
countElementInList([1,2,3,4,2,3,2],True)
countElementInList(['somesh','kumar','somesh'],'somesh')