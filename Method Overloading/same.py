class MyClass:
    def my_method(self, a, b):
        print("First:", a + b)

    def my_method(self, a, b):
        print("Second:", a * b)

obj = MyClass()
obj.my_method(2, 3) # Only the second definition is used