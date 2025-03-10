class Test:
    def func(self, a, b=None):
        if b is None:
            print("Int:", a)
        else:
            print("Int, Str:", a, b)

t = Test()
t.func(5)
t.func(5, "hello")