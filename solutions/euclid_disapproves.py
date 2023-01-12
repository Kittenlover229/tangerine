from math import pi, cos

a = int(input())
b = int(input())
angle = int(input())
angle_rad = (angle / 180) * pi
c2 = a**2 + b**2 - 2 * a * b * cos(angle_rad)
print(c2**0.5)
