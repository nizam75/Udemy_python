def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b

def divide(a,b):
    return a/b

def exponent(a, b):
    return a **b
def calculator():
    operations = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide,
        "^": exponent
    }
    num1 = int(input("Enter first number:"))
    for symbol in operations:
        print(symbol)
    should_continue = True
    while should_continue:
        operation_symbol = input("Pick any operation symbol you want to perform operation: ")
        num2 = int(input("Enter next number:"))
        function_calculator = operations[operation_symbol]
        answer = function_calculator(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        if input(f"Enter 'y' if you want to perform more operation with {answer} or press 'n' ") == 'y':
            num1 = answer
        else:
            should_continue = False
            calculator()

calculator()