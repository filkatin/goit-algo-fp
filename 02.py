import turtle
import math

# Функція для малювання фрактала "дерево Піфагора"
def draw_pythagoras_tree(t, branch_length, angle, depth):
    if depth == 0:
        return

    # Малюємо основну гілку
    t.forward(branch_length)

    # Малюємо ліву гілку
    t.left(angle)
    draw_pythagoras_tree(t, branch_length * 0.7, angle, depth - 1)

    # Повертаємося до основної гілки
    t.right(2 * angle)
    draw_pythagoras_tree(t, branch_length * 0.7, angle, depth - 1)

    # Повертаємося до стовбура
    t.left(angle)
    t.backward(branch_length)

# Налаштування екрану та запит у користувача на рівень рекурсії
def main():
    screen = turtle.Screen()
    screen.title("Фрактал 'дерево Піфагора'")
    screen.setup(width=800, height=600)
    screen.bgcolor("white")

    # Запит у користувача на рівень рекурсії
    depth = int(input("Введіть рівень рекурсії для дерева Піфагора (рекомендується від 1 до 10): "))

    # Налаштування черепахи
    t = turtle.Turtle()
    t.speed(0)  # Максимальна швидкість малювання
    t.left(90)  # Поворот вгору для початку малювання дерева
    t.penup()
    t.goto(0, -250)  # Стартова позиція
    t.pendown()

    # Початкова довжина та кут нахилу
    branch_length = 100
    angle = 30

    # Малюємо фрактал
    draw_pythagoras_tree(t, branch_length, angle, depth)

    # Завершення роботи програми
    turtle.done()

# Запуск програми
main()
