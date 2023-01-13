import turtle
from math import sin, pi
t = turtle

a = int(input())
b = int(input())

for i in range(0, 200 + 1):
    t.goto(i, a * sin(pi * i / 10) + b)
