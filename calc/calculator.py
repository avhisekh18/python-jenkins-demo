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

def is_running_in_ci():
    # Detect CI by checking if common Jenkins paths exist
    return 'JENKINS_URL' in os.environ or 'BUILD_ID' in os.environ or os.environ.get('CI', '') == 'true'

def get_input(prompt, fallback=None):
    try:
        if is_running_in_ci():
            print(f"{prompt} [Using default: {fallback}]")
            return fallback
        return input(prompt)
    except EOFError:
        print(f"{prompt} [EOFError – Using default: {fallback}]")
        return fallback

print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = get_input("Enter choice (1/2/3/4): ", "1")
num1 = get_input("Enter first number: ", "5")
num2 = get_input("Enter second number: ", "3")

try:
    num1 = float(num1)
    num2 = float(num2)
except ValueError:
    print("Invalid numeric input.")
    exit(1)

if choice == '1':
    print(f"{num1} + {num2} = {num1 + num2}")
elif choice == '2':
    print(f"{num1} - {num2} = {num1 - num2}")
elif choice == '3':
    print(f"{num1} * {num2} = {num1 * num2}")
elif choice == '4':
    if num2 != 0:
        print(f"{num1} / {num2} = {num1 / num2}")
    else:
        print("Error: Division by zero")
else:
    print("Invalid input")