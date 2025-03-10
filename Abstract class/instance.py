from abc import ABC, abstractmethod

class Base(ABC):
    @abstractmethod
    def abstract_method(self):
        pass

class Child(Base):
    def abstract_method(self):
        print("Abstract method implemented in Child")

    def call_abstract(self):
        self.abstract_method()

c = Child()
c.call_abstract()