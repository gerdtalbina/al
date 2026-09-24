import turtle
turtle.shape("turtle")
turtle.speed(5)
def circle(r):
    turtle.circle(r)

turtle.penup()
turtle.goto(0, -100)
turtle.setheading(0)
turtle.pendown()

turtle.color("black", "yellow")
turtle.begin_fill()
circle(100)
turtle.end_fill()

turtle.color("red")

turtle.penup()
turtle.goto(-35, 35)
turtle.pendown()
turtle.dot(18, "blue")

turtle.penup()
turtle.goto(35, 35)
turtle.pendown()
turtle.dot(18, "blue")

turtle.penup()
turtle.goto(0, 15)
turtle.pendown()
turtle.pensize(6)
turtle.dot(12, "black")

turtle.penup()
turtle.goto(-45, -25)
turtle.setheading(-60)
turtle.pendown()
turtle.pensize(6)
turtle.circle(50, 120)
