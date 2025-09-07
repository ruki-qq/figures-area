# Figures Area

A Python library for calculating the area of geometric shapes. Currently supports circles and triangles with validation and factory pattern support.

## Installation

### From Source

```bash
git clone <repository-url>
cd figures-area
pip install -e .
```

### Development Setup

```bash
python -m venv venv
source venv/bin/activate

pip install -e .

pip install pytest
```

## Usage

### Direct Instantiation

```python
from figures_area import Circle, Triangle

circle = Circle(radius=5.0)
print(f"Circle area: {circle.area()}")  # 78.54

triangle = Triangle(a=3, b=4, c=5)
print(f"Triangle area: {triangle.area()}")  # 6.0
print(f"Is right triangle: {triangle.is_right()}")  # True
```

### Factory Pattern

```python
from figures_area import create_shape

circle = create_shape("circle", radius=3.0)
triangle = create_shape("triangle", a=6, b=8, c=10)

print(f"Circle area: {circle.area()}")  # 28.27
print(f"Triangle area: {triangle.area()}")  # 24.0
```

### Area Calculation Helper

```python
from figures_area import area_of, Circle, Triangle

circle = Circle(radius=2.0)
triangle = Triangle(a=3, b=4, c=5)

print(f"Circle area: {area_of(circle)}")  # 12.57
print(f"Triangle area: {area_of(triangle)}")  # 6.0
```

## Testing

```bash
pytest tests/ -v

pytest tests/test_shapes.py::TestCircle -v
```

### Test Structure

- **TestCircle**: Tests for circle functionality
- **TestTriangle**: Tests for triangle functionality  
- **TestFactoryFunctions**: Tests for factory pattern
