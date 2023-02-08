class Square:
    def __init__(self, long):
        self.long = long
class Shape(Square):
    def __init__(self, long):
        super().__init__(long)
    def area(self, long):
        print(self.long * 0)

long = Shape(int(input()))
long.area(long)
