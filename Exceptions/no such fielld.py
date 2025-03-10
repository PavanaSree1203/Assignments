class MyClass:
    def __init__(self, x):
        self.x = x

obj = MyClass(10)

try:
    print(obj.y)  # Attempting to access a non-existent attribute 'y'
except AttributeError:
    print("AttributeError: No such field/attribute.")