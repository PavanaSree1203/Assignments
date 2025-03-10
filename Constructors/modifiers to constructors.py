class MyClass:
    def __init__(self, public, _protected, __private, default):
        self.public = public
        self._protected = _protected
        self.__private = __private
        self.default = default

    def show(self):
        print(self.public, self._protected, self._MyClass__private, self.default)

obj = MyClass(1, 2, 3, 4)
obj.show()

print(obj.public)
print(obj._protected)
print(obj._MyClass__private)
print(obj.default)