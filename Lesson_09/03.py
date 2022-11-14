class Parallelogram:
    def __init__(self, width=0, length=0):
        self.width = width
        self.length = length

    def get_area(self):
        return self.width * self.length


first = Parallelogram(2, 5)
print(first.get_area())


class Square(Parallelogram):
    def get_area(self):
        return self.width ** 2


second = Square(2)
print(second.get_area())
