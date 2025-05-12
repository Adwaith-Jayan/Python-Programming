from images import Image
image=Image("daffodils.gif")
image.draw()
new=image.clone()
def edgeDetect(amount):
    black=(0,0,0)
    white=(255,255,255) 
    def average(triple):
        r,g,b=triple
        return (r+g+b)//3
    for y in range(image.getHeight()-1):
        for x in range(1,image.getWidth()):
            oldPixel=image.getPixel(x,y)
            left=image.getPixel(x-1,y)
            bottom=image.getPixel(x,y+1)
            leftlum=average(left)
            oldlum=average(oldPixel)
            bottomlum=average(bottom)
            if abs(oldlum - leftlum) > amount or abs(oldlum-bottomlum) > amount:
                new.setPixel(x,y,black)
            else:
                new.setPixel(x,y,white)
    new.draw()

edgeDetect(10)


