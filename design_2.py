import turtle
turtle.bgcolor('black')
turtle.speed(0)
turtle.pensize(5)

for i in range(6):
    for colours in("red","magenta","blue","cyan","green","white"):
        turtle.color(colours)
        turtle.circle(100)
        turtle.left(10)
turtle.hideturtle()
turtle.done()