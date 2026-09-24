import turtle
import math
turtle.shape("turtle")
turtle.speed(5)
def polygon(n, r):
    points = []
    for i in range(n):
        angle = 2 * math.pi * i / n
        x = r * math.cos(angle)
        y = r * math.sin(angle)
        points.append((x, y))
    turtle.penup()
    turtle.goto(points[0])
    turtle.pendown()
    for point in points[1:]:
        turtle.goto(point)
    turtle.goto(points[0])
for n in range(3, 13):
    polygon(n, 15 + (n - 3) * 12)
