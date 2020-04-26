class Student:
    school = 'Murodjon'
    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
    def avg(self):
        return (self.m1 + self.m2 + self.m3)/3
    @classmethod
    def info(cls):
        return cls.school
    @staticmethod
    def studinfo():
        print("This is the static method")

s1 = Student(55,13,47)
s2 = Student(12,85,15)

print(s1.avg())
print(s2.avg())
print(Student.info())
Student.studinfo()