def example():
    try:
        print("Try")
        return 1
    finally:
        print("Finally")
        return 2

result = example()
print("Result:", result)