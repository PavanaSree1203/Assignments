from abc import ABC, abstractmethod

class Base(ABC):
    def non_abstract(self):
        print("Non-abstract method")

    @abstractmethod
    def abstract_method(self):
        pass

class Derived(Base):
    def abstract_method(self):
        print("Abstract method implemented")

# Example usage:
derived_obj = Derived()
derived_obj.non_abstract()