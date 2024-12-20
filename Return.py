def calculate_product(num1, num2):
    return num1 * num2

def main():
    try:
        # Take input from the user
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        
        # Calculate the product
        product = calculate_product(num1, num2)
        
        # Display the result
        print(f"The product of {num1} and {num2} is {product:.2f}.")
    except ValueError:
        print("Please enter valid numbers.")

if __name__ == "__main__":
    main()