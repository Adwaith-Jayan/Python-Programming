from images import Image

image=Image("daffodils.gif")
image.draw()
def Shrink(factor):
    width=image.getWidth()
    height=image.getHeight()
    new=Image(width//factor,height//factor)
    oldY=0
    newY=0
    while oldY < height -factor:
        newX=0
        oldX=0
        while oldX < width-factor:
            pix=image.getPixel(oldX,oldY)
            new.setPixel(newX,newY,pix)
            oldX+=factor
            newX+=1
        oldY+=factor
        newY+=1
    new.draw()
Shrink(3)