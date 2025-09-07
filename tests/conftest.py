import math

import pytest

from figures_area import Circle, Triangle


@pytest.fixture
def sample_circle():
    """A circle with radius 3 for testing"""

    return Circle(radius=3)


@pytest.fixture
def sample_triangle_345():
    """A right triangle with sides 3, 4, 5"""

    return Triangle(a=3, b=4, c=5)


@pytest.fixture
def sample_triangle_general():
    """A general triangle with sides 7, 8, 9"""

    return Triangle(a=7, b=8, c=9)


@pytest.fixture
def right_triangles():
    """List of right triangles for testing"""

    return [
        Triangle(a=3, b=4, c=5),
        Triangle(a=5, b=12, c=13),
        Triangle(a=7, b=24, c=25),
        Triangle(a=8, b=15, c=17),
    ]


@pytest.fixture
def invalid_triangles():
    """List of invalid triangle configurations for testing"""

    return [
        {"a": 1, "b": 2, "c": 3},
        {"a": -1, "b": 2, "c": 2},
        {"a": 0, "b": 2, "c": 2},
        {"a": 1, "b": 1, "c": 3},
    ]


@pytest.fixture
def invalid_circles():
    """List of invalid circle configurations for testing"""

    return [
        {"radius": 0},
        {"radius": -1},
        {"radius": -0.5},
    ]


@pytest.fixture
def circle_test_cases():
    """Test cases for circles with expected areas"""

    return [
        {"radius": 1, "expected_area": math.pi},
        {"radius": 2, "expected_area": math.pi * 4},
        {"radius": 3, "expected_area": math.pi * 9},
        {"radius": 0.5, "expected_area": math.pi * 0.25},
    ]


@pytest.fixture
def triangle_test_cases():
    """Test cases for triangles with expected areas"""

    return [
        {"a": 3, "b": 4, "c": 5, "expected_area": 6.0},
        {"a": 5, "b": 12, "c": 13, "expected_area": 30.0},
        {"a": 6, "b": 8, "c": 10, "expected_area": 24.0},
    ]


@pytest.fixture
def factory_test_cases():
    """Test cases for factory functions"""

    return [
        {"type": "circle", "params": {"radius": 2}, "expected_class": Circle},
        {
            "type": "triangle",
            "params": {"a": 3, "b": 4, "c": 5},
            "expected_class": Triangle,
        },
    ]
