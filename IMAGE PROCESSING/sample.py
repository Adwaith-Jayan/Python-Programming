from images import Image
from functools import reduce

def blur(image):

    def triplesum(tuple1,tuple2):
        r1,g1,b1=tuple1
        r2,g2,b2=tuple2
        return r1+r2,g1+g2,b1+b2

    for y in range(1,image.getHeight()-1):
        for x in range(1,image.getWidth()-1):
            oldP=image.getPixel(x,y)
            left=image.getPixel(x-1,y)
            right=image.getPixel(x+1,y)
            top=image.getPixel(x,y+1)
            bottom=image.getPixel(x,y-1)
            sum=(reduce(triplesum,[oldP,left,right,top,bottom]))
            avg=tuple(map(lambda x:x //5,sum))
            image.setPixel(x,y,avg)
    image.draw()

filename=input("Enter image name .gif:")
image=Image(filename)
new=image.clone()
blur(new)
image.draw()
