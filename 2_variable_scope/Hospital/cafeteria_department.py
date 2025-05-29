#Global variable
menu = "sandwich,salad,soup,drink"

# function syntax
# def function_name(parameters):
#   return value

def billingCounter():
    global menu
    print("Welcome to the billing counter!")
    print("Available menu items:", menu)
    menu = menu+(",bonda")  # Adding a new item to the menu
    print("Updated menu items:", menu)

def cookingCorner():
    #Enclosing the variable scope bonda_quantity within the function scope
    bonda_quantity = 10
    print("Cooking your order...")
    print("Available menu items:", menu)
    def cookBonda():
        bonda_quantity = 15         
        print(f"Cooking {bonda_quantity} bondas...")   
    cookBonda()  # Calling the inner function to cook bonda
    print("Bonda is ready to be served!")



def servingPlace():
    #Local variable scope for serving
    bonda_order_for_customer = 5
    global menu
    print("Your order is ready to be served!")
    print("Available menu items:", menu)
    menu = menu.replace(",bonda","")  # Removing an item from the menu
    print("Updated menu items:", menu)
    print(f"Serving {bonda_order_for_customer} bondas to the customer...")

def customerOrder():
    print("Please place your order from the menu:")
    print("Available menu items:", menu)
    
billingCounter()
cookingCorner()
servingPlace()  
customerOrder()