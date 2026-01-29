def run_safe_calculator():
    """
    Function to perform exception-safe calculations.
    Refactored from Task 2 requirements.
    """
    try:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        op = input("Choose operator (+ - * /): ")
        
        if op == '+':
            result = num1 + num2
        elif op == '-':
            result = num1 - num2
        elif op == '*':
            result = num1 * num2
        elif op == '/':
            result = num1 / num2
        else: 
            print("Invalid operator")
            result = None
            
    # Exception handling as per Task 2 requirements
    except ValueError:
        print("Error: Please enter valid numerical inputs.")
        result = None
    except ZeroDivisionError:
        print("Error: A number cannot be divided by zero.")
        result = None
    else:    
        if result is not None:
            print(f"The result is: {result}")
    finally:
        print("Calculation attempt finished.")