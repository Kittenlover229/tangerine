import turtle

L = int(input())
N = int(input())

for i in range(1 + N * 2):
    turtle.forward(L)
    if turtle.isdown():
        turtle.penup()
    else:
        turtle.pendown()

turtle.exitonclick()
