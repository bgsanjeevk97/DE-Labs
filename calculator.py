def add(x, y):
    """Add two numbers"""
    return x + y

def subtract(x, y):
    """Subtract two numbers"""
    return x - y

def multiply(x, y):
    """Multiply two numbers"""
    return x * y

def divide(x, y):
    """Divide two numbers"""
    if y == 0:
        return "Error: Cannot divide by zero"
    return x / y

def power(x, y):
    """Raise x to the power of y"""
    return x ** y

def modulus(x, y):
    """Get remainder of division"""
    if y == 0:
        return "Error: Cannot divide by zero"
    return x % y

def calculator():
    """Main calculator function"""
    print("=" * 40)
    print("       SIMPLE CALCULATOR")
    print("=" * 40)
    
    while True:
        print("\nSelect operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Power")
        print("6. Modulus")
        print("7. Exit")
        
        choice = input("\nEnter choice (1/2/3/4/5/6/7): ").strip()
        
        if choice == '7':
            print("\nThank you for using the calculator!")
            break
        
        if choice in ('1', '2', '3', '4', '5', '6'):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                
                if choice == '1':
                    print(f"\n{num1} + {num2} = {add(num1, num2)}")
                
                elif choice == '2':
                    print(f"\n{num1} - {num2} = {subtract(num1, num2)}")
                
                elif choice == '3':
                    print(f"\n{num1} × {num2} = {multiply(num1, num2)}")
                
                elif choice == '4':
                    result = divide(num1, num2)
                    print(f"\n{num1} ÷ {num2} = {result}")
                
                elif choice == '5':
                    print(f"\n{num1} ^ {num2} = {power(num1, num2)}")
                
                elif choice == '6':
                    result = modulus(num1, num2)
                    print(f"\n{num1} % {num2} = {result}")
            
            except ValueError:
                print("\nInvalid input! Please enter numeric values.")
        else:
            print("\nInvalid choice! Please select 1-7. Or just get lost")

if __name__ == "__main__":
    calculator()
