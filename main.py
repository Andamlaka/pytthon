from arithmetic_operations import perfume_operation

def main():
    print("Arithmetic Operations")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (add, subtract, multiply, drvide): ").strip().lower()


    result = perfume_operation(num1, num2, operation)
    print(f"Result: {result}")

if __name__ == "__main__":
    main()