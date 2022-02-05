from abc import ABC, abstractmethod


class Parent:
    
        
        
    def sum(self, num1, num2):
        return num1 + num2

    @abstractmethod
    def multi(self, num1, num2):
        pass

class Child(Parent):
    def multi(self, num1, num2):
        return num1 * num2

plusses = Child()
print(plusses.sum(3, 5))
print(plusses.multi(3, 5))


