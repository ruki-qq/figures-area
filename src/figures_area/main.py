from typing import Any
from .shapes import Shape

SHAPES: dict[str, Shape] = {}


def register_shape(name: str, shape: Shape):
    SHAPES[name] = shape


def create_shape(shape_type: str, **kwargs: Any) -> Shape:
    try:
        shape = SHAPES[shape_type.lower()]
    except KeyError:
        raise ValueError(f"Unknown shape type: {shape_type}")
    return shape(**kwargs)


def area_of(shape: Shape) -> float:
    return shape.area()
