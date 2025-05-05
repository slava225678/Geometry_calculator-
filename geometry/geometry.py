import math
from abc import ABC, abstractmethod


class Shape(ABC):
    """Abstract base class for all shapes"""

    @abstractmethod
    def get_area(self) -> float:
        """Calculate and return the area of the shape"""
        pass

    @abstractmethod
    def is_valid(self) -> bool:
        """Check if the shape is valid"""
        pass


class Circle(Shape):
    """Circle shape defined by radius"""

    def __init__(self, radius: float):
        self.radius = radius

    def get_area(self) -> float:
        if not self.is_valid():
            raise ValueError("Invalid circle: radius must be positive")
        return math.pi * self.radius ** 2

    def is_valid(self) -> bool:
        return self.radius > 0


class Triangle(Shape):
    """Triangle shape defined by three sides"""

    def __init__(self, side_a: float, side_b: float, side_c: float):
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def get_area(self) -> float:
        if not self.is_valid():
            raise ValueError("Invalid triangle sides")

        # Heron's formula
        s = (self.side_a + self.side_b + self.side_c) / 2
        return math.sqrt(
            s * (s - self.side_a) * (s - self.side_b) * (s - self.side_c)
         )

    def is_valid(self) -> bool:
        """Check if triangle is valid using triangle inequality theorem"""
        a, b, c = self.side_a, self.side_b, self.side_c
        return (a > 0 and b > 0 and c > 0 and
                a + b > c and
                a + c > b and
                b + c > a)

    def is_right(self, tolerance: float = 1e-6) -> bool:
        """Check if triangle is right-angled using Pythagorean theorem"""
        if not self.is_valid():
            return False
        # Sort sides to find hypotenuse (longest side)
        a, b, c = sorted([self.side_a, self.side_b, self.side_c])
        # Check Pythagorean theorem with
        # some tolerance for floating point precision
        return abs(a**2 + b**2 - c**2) < tolerance


def calculate_area(shape: Shape) -> float:
    """Calculate area of any shape without knowing its type at compile time"""
    return shape.get_area()
