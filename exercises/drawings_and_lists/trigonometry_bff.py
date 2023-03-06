import turtle
from math import sin, pi

a = int(input())
b = int(input())

for i in range(0, 200 + 1):
    turtle.goto(i, a * sin(pi * i / 10) + b)
print(turtle.pos())

turtle.exitonclick()
