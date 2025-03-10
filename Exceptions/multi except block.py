def process_data(data):
    try:
        result = 10 / data[0]
        value = int(data[1])
        print("Result:", result, "Value:", value)
    except ZeroDivisionError:
        print("Error: Division by zero.")
    except IndexError:
        print("Error: Index out of range.")
    except ValueError:
        print("Error: Invalid value.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

process_data([1, "5"])
process_data([0, "5"])
process_data([1])
process_data([1, "abc"])
process_data(None)