import turtle
t = turtle

A = int(input())
N = int(input())

sidelen = A * 5

for i in range(N):
    t.forward(sidelen)
    t.right(360/N)
