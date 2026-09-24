import turtle
turtle.shape('turtle')
turtle.speed(5)
def circle(x, y, r):
    turtle.penup()
    turtle.goto(x, y - r)
    turtle.setheading(0)
    turtle.pendown()
    turtle.circle(r)
for r in range(20, 101, 10):
    circle(-r, 0, r)
for r in range(20, 101, 10):
    circle(r, 0, r)
