from abc import ABC, abstractmethod

class Computer(ABC):
    @abstractmethod
    def process(self):
        pass
class Laptop(Computer):
    def process(self):
        print("Running")


class Programmer:
    def work(self,com):
        print("Solving a problem")
        com.process()

com1 = Laptop()
com2 = Programmer()


com2.work(com1)