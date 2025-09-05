from dataclasses import dataclass
from math import sqrt

from .base import Shape


@dataclass()
class Triangle(Shape):
    # sides lengths
    a: float
    b: float
    c: float

    def __post_init__(self):
        a, b, c = self.a, self.b, self.c

        if min(a, b, c) <= 0:
            raise ValueError("Triangle sides must be positive")
        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError("Triangle is not valid")

    def area(self) -> float:
        # Heron's formula
        # s: semiperimeter
        s = (self.a + self.b + self.c) / 2.0

        return sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def is_right(self) -> bool:
        """Checks if the triangle is right angled using Pythagorean theorem"""

        a, b, c = sorted([self.a, self.b, self.c])
        return c * c == b * b + a * a
