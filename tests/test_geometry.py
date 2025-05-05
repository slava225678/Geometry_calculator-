import pytest
import math
from geometry.geometry import Circle, Triangle, calculate_area


class TestCircle:
    def test_valid_circle_area(self):
        circle = Circle(5)
        assert math.isclose(circle.get_area(), 78.539816, rel_tol=1e-6)

    def test_zero_radius(self):
        circle = Circle(0)
        assert not circle.is_valid()
        with pytest.raises(ValueError):
            circle.get_area()

    def test_negative_radius(self):
        circle = Circle(-1)
        assert not circle.is_valid()
        with pytest.raises(ValueError):
            circle.get_area()


class TestTriangle:
    def test_valid_triangle_area(self):
        triangle = Triangle(3, 4, 5)
        assert math.isclose(triangle.get_area(), 6.0, rel_tol=1e-6)

    def test_right_triangle_check(self):
        assert Triangle(3, 4, 5).is_right()
        assert Triangle(5, 12, 13).is_right()
        assert not Triangle(5, 5, 5).is_right()

    def test_invalid_triangle(self):
        assert not Triangle(1, 2, 3).is_valid()
        assert not Triangle(0, 0, 0).is_valid()
        assert not Triangle(-1, 2, 2).is_valid()

        with pytest.raises(ValueError):
            Triangle(1, 2, 3).get_area()

    def test_equilateral_triangle(self):
        triangle = Triangle(2, 2, 2)
        assert math.isclose(triangle.get_area(), math.sqrt(3), rel_tol=1e-6)


class TestCalculateArea:
    def test_polymorphic_area_calculation(self):
        shapes = [Circle(2), Triangle(3, 4, 5)]
        areas = [calculate_area(shape) for shape in shapes]
        assert math.isclose(areas[0], 12.566371, rel_tol=1e-6)
        assert math.isclose(areas[1], 6.0, rel_tol=1e-6)
