import turtle
turtle.shape('turtle')
turtle.speed(5)
def star(n, length):
    angle = 180 - 180 / n
    for i in range(n):
        turtle.forward(length)
        turtle.right(angle)
star(5, 100)

turtle.penup()
turtle.goto(200, 0)
turtle.setheading(0)
turtle.pendown()

star(11, 100)