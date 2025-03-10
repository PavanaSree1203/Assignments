class Super:
    def __init__(self, arg=None):
        print("Super:", arg if arg else "Default")

class Child(Super):
    def __init__(self, arg1=None, arg2=None):
        super().__init__(arg1)
        print("Child:", arg2 if arg2 else "Default")

Child()
Child(1)
Child(1, 2)