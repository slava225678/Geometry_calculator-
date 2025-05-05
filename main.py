from geometry.geometry import Circle, Triangle, calculate_area


def main():
    # Пример работы с кругом
    print("=== Пример работы с кругом ===")
    circle = Circle(5)
    print(f"Площадь круга с радиусом 5: {circle.get_area():.2f}")
    print(f"Валидность круга: {circle.is_valid()}")

    # Пример работы с треугольником
    print("\n=== Пример работы с треугольником ===")
    triangle = Triangle(3, 4, 5)
    print(
        f"Площадь треугольника со сторонами 3,4,5: {triangle.get_area():.2f}"
     )
    print(f"Прямоугольный ли треугольник: {triangle.is_right()}")
    print(f"Валидность треугольника: {triangle.is_valid()}")

    # Универсальный расчет площади
    print("\n=== Универсальный расчет площади ===")
    shapes = [Circle(2), Triangle(3, 4, 5), Circle(1.5)]
    for shape in shapes:
        print(f"Площадь фигуры: {calculate_area(shape):.2f}")


if __name__ == "__main__":
    main()
