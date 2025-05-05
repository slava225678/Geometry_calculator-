# Geometry Area Calculator

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code Style: Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Библиотека для вычисления площадей геометрических фигур с поддержкой различных операций.

## Оглавление

- [Установка](#установка)
- [Быстрый старт](#быстрый-старт)
- [Документация](#документация)
  - [Круг](#круг)
  - [Треугольник](#треугольник)
  - [Универсальный расчет площади](#универсальный-расчет-площади)
- [Расширение библиотеки](#расширение-библиотеки)
- [Тестирование](#тестирование)


## 1. Установка

Установите библиотеку через pip:

```bash
pip install git+https://github.com/yourusername/Geometry_calculator-.git
```
Или вручную:

```bash
git clone https://github.com/yourusername/Geometry_calculator-.git

cd Geometry_calculator-
```


### 2. Активируй виртуальное окружение

Windows:

```bash
python -m venv venv
sourse venv/Scripts/activate
```

Linux/macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Установи зависимости

```bash
pip install -r requirements.txt
```
## Быстрый старт

```python
from geometry import Circle, Triangle, calculate_area

# Пример работы с кругом
circle = Circle(radius=5)
print(f"Площадь круга: {circle.get_area():.2f}")
print(f"Валиден: {circle.is_valid()}")

# Пример работы с треугольником
triangle = Triangle(3, 4, 5)
print(f"Площадь треугольника: {triangle.get_area():.2f}")
print(f"Прямоугольный: {triangle.is_right()}")
print(f"Валиден: {triangle.is_valid()}")

# Универсальный расчет
shapes = [Circle(2), Triangle(3, 4, 5)]
areas = [calculate_area(shape) for shape in shapes]
```
## Документация
### Круг
Класс `Circle` представляет геометрическую фигуру окружности.

```python
Circle(radius: float)
```
Параметры:

`radius` - положительное число, радиус окружности

Методы:

`get_area() -> float` - возвращает площадь круга

`is_valid() -> bool` - проверяет валидность круга

Пример:

```python
circle = Circle(5)
area = circle.get_area()  # 78.53981633974483
```
### Треугольник
Класс `Triangle` представляет геометрическую фигуру треугольника.

```python
Triangle(side_a: float, side_b: float, side_c: float)
```
Параметры:

`side_a`, `side_b`, `side_c` - длины сторон треугольника (положительные числа)

Методы:

`get_area() -> float` - возвращает площадь треугольника

`is_valid() -> bool` - проверяет валидность треугольника

`is_right(tolerance: float = 1e-6) -> bool` - проверяет, является ли треугольник прямоугольным

Пример:

```python
triangle = Triangle(3, 4, 5)
area = triangle.get_area()  # 6.0
is_right = triangle.is_right()  # True
```
### Универсальный расчет площади
Функция `calculate_area` позволяет вычислять площадь без явного указания типа фигуры:

```python
def calculate_area(shape: Shape) -> float
```
Пример:

```python
shapes = [Circle(2), Triangle(3, 4, 5)]
areas = [calculate_area(shape) for shape in shapes]  # [12.566..., 6.0]
```
## Расширение библиотеки
Чтобы добавить новую фигуру:

1. Создайте класс, унаследованный от Shape

2. Реализуйте обязательные методы:

    `get_area()` - должен возвращать площадь фигуры

    `is_valid()` - должен проверять валидность фигуры

Пример добавления квадрата:

```python
from geometry import Shape

class Square(Shape):
    def __init__(self, side: float):
        self.side = side
    
    def get_area(self) -> float:
        if not self.is_valid():
            raise ValueError("Side must be positive")
        return self.side ** 2
    
    def is_valid(self) -> bool:
        return self.side > 0
```
## Тестирование
Библиотека включает полный набор юнит-тестов. Для запуска:

```bash
pytest tests/ -v
```
Для проверки покрытия кода тестами:

```bash
pytest --cov=geometry tests/
```