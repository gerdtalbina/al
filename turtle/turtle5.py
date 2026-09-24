import turtle
turtle.shape('turtle')
for i in range(10):
    for j in range(4):
        turtle.forward(200 - i * 20)
        turtle.left(90)
    turtle.penup()
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(10)
    turtle.right(90)
    turtle.pendown()
