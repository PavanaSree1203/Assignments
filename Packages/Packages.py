# my_program.py

class Class1:
    def __init__(self, name):
        self.name = name

    def method1(self):
        print(f"Method 1 called from Class1, name: {self.name}")

class Class2:
    def __init__(self, value):
        self.value = value

    def method2(self):
        print(f"Method 2 called from Class2, value: {self.value}")

if __name__ == "__main__":
    obj1 = Class1("Object 1")
    obj1.method1()

    obj2 = Class2(42)
    obj2.method2()