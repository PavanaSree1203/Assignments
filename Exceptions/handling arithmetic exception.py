def divide(a, b):
    try:
        result = a / b
        return result
    except ArithmeticError:
        print("Error: Division by zero or other arithmetic problem.")
        return None  # Or some other default value

result1 = divide(10, 2)
print(result1)

result2 = divide(10, 0)
print(result2)