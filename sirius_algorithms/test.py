class Parent:

    def __init__(self):
        self.counter = 0

    def inc(self):
        self.counter += 1

class Test(Parent):

    def __init__(self):
        self.counter = 10

    def dec(self):
        self.counter -= 1


t = Test()
print(t.counter)
t.inc()
print(t.counter)