from dataclasses import dataclass
from math import pi

from .base import Shape


@dataclass
class Circle(Shape):
    radius: float

    def __post_init__(self):
        if self.radius <= 0:
            raise ValueError("Radius must be positive")

    def area(self) -> float:
        return pi * (self.radius**2)
