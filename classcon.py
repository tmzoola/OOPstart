class Student:
    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.Laptop()
    def show(self):
        print(self.name, self.rollno)

    class Laptop:
        def __init__(self):
            self.brand = 'HP'
            self.cpu = '15'
            self.ram = 8
        def show(self):
            print(self.brand, self.ram, self.cpu)

s1 = Student('Murodjon',5)
s2 = Student('tulesko',25)
lap1 = Student.Laptop()
s1.show()
lap1.show()