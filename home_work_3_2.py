import turtle

def koch_snowflake(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_snowflake(t, order-1, size/3)
            t.left(angle)

def main():
    screen = turtle.Screen()
    screen.setup(800, 600)

    t = turtle.Turtle()
    t.speed(0)

    # Level of recursion
    recursion_level = int(input("Введіть рівень рекурсії для сніжинки Коха: "))

    # Start point
    t.penup()
    t.goto(-150, 90)
    t.pendown()

    # Drawing snowflake
    for i in range(3):
        koch_snowflake(t, recursion_level, 300)
        t.right(120)

    screen.mainloop()

if __name__ == "__main__":
    main()
