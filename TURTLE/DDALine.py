from turtle import *

x1, y1 = map(int, input("Enter x1 and y1: ").split())
x2, y2 = map(int, input("Enter x2 and y2: ").split())

# Use float division
m = (y2 - y1) / (x2 - x1)
print("Slope:", m)

x, y = x1, y1
t = Turtle()
t.speed(0)
t.penup()
t.goto(x, y)
t.pendown()

if abs(m - 1) < 1e-6:
    while x <= x2 and y <= y2:
        t.goto(x, y)
        x += 1
        y += 1
elif abs(m) < 1:
    while x <= x2:
        t.goto(x, y)
        x += 1
        y += m
else:
    while y <= y2:
        t.goto(x, y)
        x += 1/m
        y += 1

done()
