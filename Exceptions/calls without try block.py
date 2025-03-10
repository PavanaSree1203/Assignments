class MyClass:
    def throw_exception(self):
        raise ValueError("This is a raised exception")

class Main:
    def run(self):
        obj = MyClass()
        obj.throw_exception() # Calling the method without a try block

if __name__ == "__main__":
    main_instance = Main()
    main_instance.run()