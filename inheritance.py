class A:
    def __init__(self):
        print("in init")

    def feature1(self):
        print("Feature 1 is working")
    def feature2(self):
        print("Feature 2 is working")

class B:
    def __init__(self):
        print("in B init")
    def feature3(self):
        print("Feature 3 is working")
    def feature4(self):
        print("Feature 4 is working")

class C(A,B):
    def __init__(self):
        super().__init__()
        print("in C Init")


a1 = C()



