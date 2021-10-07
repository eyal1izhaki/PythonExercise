class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __eq__(self, other):
        return (self.x == other.x) and (self.y == other.y)

    def __add__(self, other):
        return Point(self.x+other.x, self.y+other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"
