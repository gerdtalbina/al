import turtle
turtle.shape('turtle')
turtle.speed(5)
def circle(radius):
    turtle.circle(radius)
for i in range(6):
    circle(50)
    turtle.left(60)
