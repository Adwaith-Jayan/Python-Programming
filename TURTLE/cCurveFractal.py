from turtle import Turtle,Screen

def cCurve(t,x1,y1,x2,y2,level):
    def drawline(t,x1,y1,x2,y2):
        t.up()
        t.goto(x1,y1)
        t.down()
        t.goto(x2,y2)
    if level==1:
        drawline(t,x1,y1,x2,y2)
    else:
        xm=(x1+x2+y1-y2)//2
        ym=(x2+y1+y2-x1)//2
        cCurve(t,x1,y1,xm,ym,level-1)
        cCurve(t,xm,ym,x2,y2,level-1)


def main():
    t=Turtle()
    level=int(input("Enter level:"))
    cCurve(t,50,-50,50,50,level)

main()
Screen().exitonclick()