
def outter():
    msg = "Hello from outer function"
    print("Outer function called, message:", msg)
    def inner():
        nonlocal msg
        msg = "Hello from inner function"
        print("Inner function called, message:", msg)
        def inner_inner():
            nonlocal msg
            msg = "Hello from inner_inner function"
            print("Inner inner function called, message:", msg)
        inner_inner()
    inner()
    print("Outer function called, message:", msg)
    

# outter()

def parent():
    list_name = "Groceries"

    def child():
        # nonlocal list_name  # Use the parent's variable, not a new one
        list_name = "Electronics"  # Change it
        print("Inside child:", list_name)

    child()
    print("Inside parent:", list_name)
    

# parent()

def get_middle_three_chars(str1):
    print("Original String is", str1)

    # first get middle index number
    mi = int(len(str1) / 2)

    # use string slicing to get result characters
    res = str1[mi - 1:mi + 2]
    print("Middle three chars are:", res)

get_middle_three_chars("JhonDipPeta1")
get_middle_three_chars("JaSonAy1")

