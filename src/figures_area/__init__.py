__all__ = ["Shape", "Circle", "Triangle", "area_of", "create_shape"]

from .main import area_of, create_shape, register_shape
from .shapes import Shape
from .shapes import Circle
from .shapes import Triangle

register_shape("circle", Circle)
register_shape("triangle", Triangle)
