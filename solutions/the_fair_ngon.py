from math import pi, cos, sin
import turtle

A = int(input())
N = int(input())
sidelen = A * 10
d_angle = 2 * pi / N

x = 0
y = 0
angle = 0

for i in range(N):
    x += sidelen * cos(angle - d_angle) + sidelen * sin(angle - d_angle)
    y -= sidelen * sin(angle - d_angle) - sidelen * cos(angle - d_angle)
    angle -= d_angle
    turtle.goto(x, y)
