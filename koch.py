import turtle

def koch(a, depth):
    if depth == 0:
        turtle.forward(a)
        return

    koch(a/3, depth-1)
    turtle.left(60)
    koch(a/3, depth-1)
    turtle.right(120)
    koch(a/3, depth-1)
    turtle.left(60)
    koch(a/3, depth-1)

for i in range(3):
    koch(100, 2)
    turtle.right(120)

turtle.speed(500)

turtle.exitonclick()
