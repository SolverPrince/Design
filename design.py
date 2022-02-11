import turtle
turtle.bgcolor('black')
turtle.speed(0)
turtle.pensize(3)
turtle.pencolor('red')

def draw(radius):
    for i in range(10):
        turtle.circle(radius)
        radius=radius-4

def dra():
    for i in range(10):
        draw(150)
        turtle.right(36)

dra()
turtle.done()