import math

import pytest
from figures_area import Circle, Triangle, area_of, create_shape


class TestCircle:
    """Test cases for Circle class"""

    def test_circle_area_basic(self, sample_circle):
        """Test basic circle area calculation"""

        assert sample_circle.area() == math.pi * 9

    def test_circle_area_multiple_cases(self, circle_test_cases):
        """Test circle area calculation with multiple test cases"""

        for case in circle_test_cases:
            circle = Circle(radius=case["radius"])
            assert circle.area() == case["expected_area"]

    def test_circle_invalid_radius(self, invalid_circles):
        """Test circle validation with invalid radius values"""

        for invalid_config in invalid_circles:
            with pytest.raises(ValueError):
                Circle(**invalid_config)


class TestTriangle:
    """Test cases for Triangle class"""

    def test_triangle_area_345(self, sample_triangle_345):
        """Test area calculation for 3-4-5 right triangle"""

        assert sample_triangle_345.area() == 6.0

    def test_triangle_area_general(self, sample_triangle_general):
        """Test area calculation using Heron's formula"""

        s = (7 + 8 + 9) / 2.0
        expected = math.sqrt(s * (s - 7) * (s - 8) * (s - 9))
        assert sample_triangle_general.area() == expected

    def test_triangle_area_multiple_cases(self, triangle_test_cases):
        """Test triangle area calculation with multiple test cases"""

        for case in triangle_test_cases:
            triangle = Triangle(a=case["a"], b=case["b"], c=case["c"])
            assert triangle.area() == case["expected_area"]

    def test_triangle_validation(self, invalid_triangles):
        """Test triangle validation with invalid configurations"""

        for invalid_config in invalid_triangles:
            with pytest.raises(ValueError):
                Triangle(**invalid_config)

    def test_triangle_is_right_true(self, right_triangles):
        """Test right triangle detection for known right triangles"""

        for triangle in right_triangles:
            assert triangle.is_right()


class TestFactoryFunctions:
    """Test cases for factory functions"""

    def test_create_shape_circle(self, factory_test_cases):
        """Test create_shape function for circles"""

        circle_case = next(
            case for case in factory_test_cases if case["type"] == "circle"
        )
        shape = create_shape(circle_case["type"], **circle_case["params"])
        assert isinstance(shape, circle_case["expected_class"])
        assert area_of(shape) == math.pi * 4

    def test_create_shape_triangle(self, factory_test_cases):
        """Test create_shape function for triangles"""

        triangle_case = next(
            case for case in factory_test_cases if case["type"] == "triangle"
        )
        shape = create_shape(triangle_case["type"], **triangle_case["params"])
        assert isinstance(shape, triangle_case["expected_class"])
        assert area_of(shape) == 6.0

    def test_create_shape_invalid_type(self):
        """Test create_shape function with invalid shape type"""

        with pytest.raises(ValueError, match="Unknown shape type"):
            create_shape("invalid_shape", radius=1)
