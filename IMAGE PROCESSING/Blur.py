from images import Image
from functools import reduce
image=Image("daffodils.gif")

image.draw()
def triplesum(triple1,triple2):
    x1,y1,z1=triple1
    x2,y2,z2=triple2
    return (x1+x2,y1+y2,z1+z2)
for y in range(1,image.getHeight()-1):
    for x in range(1,image.getWidth()-1):
        pixel=image.getPixel(x,y)
        top=image.getPixel(x,y-1)
        bottom=image.getPixel(x,y+1)
        left=image.getPixel(x-1,y)
        right=image.getPixel(x+1,y)
        sums=reduce(triplesum,[pixel,top,bottom,left,right])
        newpixel=tuple(map(lambda x:x//5,sums))
        image.setPixel(x,y,newpixel)
image.draw()