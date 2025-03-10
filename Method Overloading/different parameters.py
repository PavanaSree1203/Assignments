class MyClass:
    def my_method(self, a, b=None):
        if b is None:
            print("One:", a)
        else:
            print("Two:", a, b)

obj = MyClass()
obj.my_method(1)
obj.my_method(1, 2)