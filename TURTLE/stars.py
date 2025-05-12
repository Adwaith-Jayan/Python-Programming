from turtle import Turtle

t=Turtle()
#five pointed star
for i in range(5):
    t.right(144)
    t.fd(50)

t.clear()
#two equilateral traingles 6 pointed star
for i in range(3):
    t.fd(100)
    t.left(120)
t.up()
t.fd(50)
t.left(90)
t.fd(55)
t.left(90)
t.fd(50)
t.right(180)
t.pendown()
for i in range(3):
    t.fd(100)
    t.right(120)

t.home()
t.clear()

t.screen.exitonclick()