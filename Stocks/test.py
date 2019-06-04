class A(object):
    def __init__(self):
        self.word = "This is A !"

    def print(self):
        print(self.word)


class B(A):
    def __init__(self):
        self.word = "This is B"

    def print(self):
        print(self.word)


class C(B):
    def __init__(self):
        self.word = "This is C"

    def print(self):
        super(B, b).print()



a = A()
b = B()
c = C()
c.print()
