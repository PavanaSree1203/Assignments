class Base:
    def non_abstract_method(self):
        print("Non-abstract method from Base")

class Child(Base):
    def call_non_abstract(self):
        self.non_abstract_method()

c = Child()
c.call_non_abstract()