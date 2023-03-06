import turtle

A = int(input())
N = int(input())

sidelen = A * 5

for i in range(N):
    turtle.forward(sidelen)
    turtle.right(360 / N)

turtle.exitonclick()
