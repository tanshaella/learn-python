import turtle
import math

print("Please enter the length of the legs in  a right triangle:")
a=float(input("Leg#1: "))
b=float(input("Leg#2: "))
c=(a**2+b**2)**0.5
alpha=math.atan(a/b)
turtle.forward(a)
turtle.left(90)
turtle.forward(b)
turtle.left(180-alpha)
turtle.forward(c)
turtle.hideturtle()
