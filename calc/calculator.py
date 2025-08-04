import os
def add(a , b):
    print("Addition function called")
    return a+b

def subtract(a , b):
    return a-b

def multiply(a , b):
    return a*b

def divide(a , b):
    if b ==0:
        raise ValueError("cannot divide by 0")
    return a/b

def get_input(prompt, fallback =None):
    try:
        return input (prompt)
    except EOFError:
        return fallback

if __name__ == '__main__':
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    
    choice = get_input("Enter choice (1/2/3/4): ")

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        print(f"The result is: {add(num1, num2)}")
    elif choice == '2':
        print(f"The result is: {subtract(num1, num2)}")
    elif choice == '3':
        print(f"The result is: {multiply(num1, num2)}")
    elif choice == '4':
        print(f"The result is: {divide(num1, num2)}")
    else:
        print("Invalid input")