import sys
import stdio
from euclid import gcd
import math


class Rational:
    def __init__(self, x, y):
        if y == 0:
            raise ValueError("Denominator cannot be zero")
        g = gcd(abs(x), abs(y))
        if g == 0:
            g = 1
        # keep sign in numerator, denominator always positive
        if y < 0:
            x, y = -x, -y
        self._x = x // g
        self._y = y // g

    def __add__(self, other):
        return Rational(self._x * other._y + other._x * self._y,
                         self._y * other._y)

    def __sub__(self, other):
        return Rational(self._x * other._y - other._x * self._y,
                         self._y * other._y)

    def __mul__(self, other):
        return Rational(self._x * other._x, self._y * other._y)

    def __abs__(self):
        return Rational(abs(self._x), abs(self._y))

    def __str__(self):
        return f"{self._x}/{self._y}"


def main():
    a = Rational(1, 2)
    b = Rational(1, 3)

    stdio.writeln("a = " + str(a))
    stdio.writeln("b = " + str(b))
    stdio.writeln("a + b = " + str(a + b))
    stdio.writeln("a - b = " + str(a - b))
    stdio.writeln("a * b = " + str(a * b))
    stdio.writeln("abs(a) = " + str(abs(a)))

    # test with negative values and reduction
    c = Rational(-4, 16)   # should reduce to -1/4
    d = Rational(6, -8)    # should reduce to -3/4
    stdio.writeln("c = " + str(c))
    stdio.writeln("d = " + str(d))
    stdio.writeln("c + d = " + str(c + d))
    stdio.writeln("abs(d) = " + str(abs(d)))


if __name__ == '__main__':
    main()