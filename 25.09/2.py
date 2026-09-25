#1/usr/bin/python3

import turtle
def circle(direction ='left'):
    N = 500
    for _ in range(N):
        turtle.forward(1)
        if direction == "left":
            turtle.left(360 / N)
        elif direction == 'right':
            turtle.right(360 / N)
        else:
                print('Error')
                return
                turtle.update()
def eight():
    circle('left')
    circle('right')

turtle.tracer(False)
turtle.shape('turtle')

N = 25
for i in range(N):
    eight()
    turtle.left(180 / N)

turtle.mainloop()
