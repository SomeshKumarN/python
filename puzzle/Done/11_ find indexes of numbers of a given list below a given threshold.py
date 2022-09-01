"""
Write a Python program to find the indexes of numbers of a given list below a given threshold.
Input:
[(100,(0, 12, 45, 3, 4923, 322, 105, 29, 15, 39, 55))]
Output:
[0, 1, 2, 3, 7, 8, 9, 10]
Input:
[(10,(0, 12, 4, 3, 49, 9, 1, 5, 3))]
Output:
[0, 2, 3, 5, 6, 7, 8]
"""

def lst(a):
    indx = []
    for i in range(len(a[0][1])):
        if a[0][1][i] < a[0][0]:
            indx.append(i)
    return indx

"""
step1->get the threashol -->100
step2->get the input value set --> (so and so)
step3->iterate the set
step3.1--> compare the set indivudual value is less than threashold
step3.2--> assign the index into a new list
step4--> return the new list which holds the indexs
"""

x = [(100,(0, 12, 45, 3, 4923, 322, 105, 29, 15, 39, 55))]
y =  [(10,(0, 12, 4, 3, 49, 9, 1, 5, 3))]
print(lst(x))
print(lst(y))

# Input:
# a =[(100,(0, 12, 45, 3, 4923, 322, 105, 29, 15, 39, 55))]
# Output:
# [0, 1, 2, 3, 7, 8, 9, 10]

#100
#100---->(==)0, 12, 45, 3, 4923, 322, 105, 29, 15, 39, 55
#100---->0, 12, 45, 3, 29, 15, 39, 55
#find index
#list(find index)