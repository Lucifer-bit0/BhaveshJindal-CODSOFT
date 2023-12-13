def input_num():
    a = int(input("Enter 1st Number: "))
    b = int(input("Enter 2nd Number: "))
    return a,b
def addition(a,b):
    print(f"Result: {a+b}")
def subtraction(a,b):
    print(f"Result: {a-b}")
def multiplication(a,b):
    print(f"Result: {a*b}")
def division(a,b):
    if b!=0:
        print(f"Result: {a/b}")
    else:
        print("Dominator can't be Zero")

def welcome():

    print(f"""Enter the arithmetic operator you want to use.
        1--> ADDITION
        2--> SUBTRACTION
        3--> MULTIPLICATION
        4--> DIVISION
        5--> exit""")

while(True):
    welcome()
    choice = int(input("Enter you choice number: "))
    if choice == 1:
        a,b = input_num()
        addition(a,b)
    elif choice==2:
        a, b = input_num()
        subtraction(a,b)
    elif choice ==3:
        a, b = input_num()
        multiplication(a,b)
    elif choice ==4:
        a, b = input_num()
        division(a,b)
    elif choice ==5:
        exit()
    else :
        print("Enter Valid Choice")