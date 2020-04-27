class Intellij:
    def execute(self):
        print("Compiling")
        print("Running")

class MyEditor:
    def execute(self):
        print("Spell Check")
        print("Compiling")
        print("Running")
        print("Compiling")
        print("Running")

class Laptop:

    def code(self,ide):
        ide.execute()

other = MyEditor()
s1 = Laptop()
s1.code(other)

