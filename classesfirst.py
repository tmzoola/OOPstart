class Computer:

    def __init__(self):
        self.name = "Murodjon"
        self.age = 28
    def update(self):
        self.age = 10
    def compare(self,other):
        if self.age == other.age:
            return True
        else:
            return False


c1 = Computer()
c1.update()
c2 = Computer()

if c1.compare(c2):
    print("they are same")
else:
    print("They are different")

print(c1.age)
print(c2.age)