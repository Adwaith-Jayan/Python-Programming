from turtle import Turtle,Screen
import math

def draw_red(t):
    t.up()
    t.home()
    t.goto(-100,100)
    t.down()
    t.begin_fill()
    t.fillcolor("red")
    for i in range(2):
        t.forward(300)
        t.right(90)
        t.forward(50)
        t.right(90)
    t.end_fill()

def draw_green(t):
    t.up()
    t.home()
    t.goto(-100,-50)
    t.down()
    t.begin_fill()
    t.fillcolor("green")
    for i in range(2):
        t.forward(300)
        t.left(90)
        t.forward(50)
        t.left(90)
    t.end_fill()


def draw_chakra(t):
    t.up()
    t.home()
    t.goto(-100,0)
    t.down()
    for i in range(2):
        t.forward(300)
        t.left(90)
        t.forward(50)
        t.left(90)
    t.pencolor("blue")
    t.up()
    t.home()
    t.goto(50,5)
    t.down()
    t.circle(20)
    t.up()
    t.goto(50, 25)
    t.down()

    for i in range(24): 
        t.up()
        angle = i * 15  
        x = 50 + 20 * math.cos(math.radians(angle))  
        y = 25 + 20 * math.sin(math.radians(angle)) 
        t.goto(50, 25)
        t.down()
        t.goto(x, y)


t=Turtle()
draw_red(t)
draw_green(t)
draw_chakra(t)
Screen().exitonclick()
