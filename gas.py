#!/usr/bin/python3

from random import randint
import turtle



number_of_turtles = 50
steps_of_time_number = 10000

border = 400

box = turtle.Turtle()
box.hideturtle()
box.penup()
box.goto(-border, -border)
box.pendown()
for _ in range(4):
    box.forward(2*border)
    box.left(90)

turtle.tracer(False)

turtle.left(60)
print(turtle.heading())

pool = [turtle.Turtle(shape='circle') for i in range(number_of_turtles)]
for unit in pool:
    unit.penup()
    unit.speed(50)
    unit.goto(randint(-border + 10, border + 10), randint(-border + 10, border + 10))
    unit.setheading(randint(0, 360))



for i in range(steps_of_time_number):
    for unit in pool:
        if abs(unit.pos()[1]) > border:
            unit.setheading(-unit.heading())
            unit.forward(1)
        if abs(unit.pos()[0]) > border:
            unit.setheading(180 - unit.heading())
            unit.forward(1)
        unit.forward(1)
    turtle.update()
