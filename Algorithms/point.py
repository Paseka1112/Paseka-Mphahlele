import math
class Point:
    """A point in two-dimensional Euclidean space."""
    def __init__(self, x, y):
        """Initialise a new Point with coordinates (x, y)."""
        self.x = x
        self.y = y
    def distance_to(self, p):
        """Return the distance from this Point to Point p."""
        dx = self.x - p.x
        dy = self.y - p.y
        return math.sqrt(dx*dx + dy*dy)
    def __str__(self):
        """x.__str__() <==> str(x)"""
        return '(' + str(self.x) + ', ' + str(self.y) + ')'

def main():
    p = Point(1, 5)
    c = Point(1,3)
    print(c.distance_to(p))

if __name__ == '__main__': main()
