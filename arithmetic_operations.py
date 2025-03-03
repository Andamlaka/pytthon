# arithmetic_operations.py

def perfume_operation(num1: float, num2: float, operation: str) -> float:
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":  # Fixed spelling from "drvide" to "divide"
        if num2 == 0:
            return "Error: Division by zero"
        return num1 / num2
    else:
        return "Error: Invalid operation"
