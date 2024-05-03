'''def add(x,y):
    return x + y

def sub(x,y):
    return x - y

def mult(x,y):
    return x * y

def divide(x,y):
    if y == 0:
       return("cannot divide by zero")
    else:
       return x / y

def display_menu():
    print("CalculTOR menu")
    print("1.Add")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    choice = input("Enter your choice(1/2/3/4/5)")
    return choice

def calclator():
    choice = display_menu()

    if choice in ('1','2','3','4'):
        num1= float(input("enter 1st num:"))
        num2 = float(input("enter 2nd num:"))

        if choice == '1':
            print("Result:",add(num1,num2))
        elif choice == '2':
            print("Result:",sub(num1,num2))
        elif choice == '3':
            print("Result:",mult(num1,num2))
        elif choice == '4':
            print("Result:",divide(num1,num2))
        calclator()

    elif choice == 5:
        print("Exiting...")
    else:
        print("Invalid input.Please enter a valid choice.")
calclator()'''


