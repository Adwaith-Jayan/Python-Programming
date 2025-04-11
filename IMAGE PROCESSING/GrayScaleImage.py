from images import Image

def toGray(image):
    for y in range(image.getHeight()):
        for x in range(image.getWidth()):
            r,g,b=image.getPixel(x,y)
            r=int(r*0.299)
            g=int(g*0.587)
            b=int(b*0.114)
            lum=r+g+b
            image.setPixel(x,y,(lum,lum,lum))
    print("Close window to exit")
    image.draw()





filename=input('Enter image name "".gif:')
image=Image(filename)
print("Close the window to continue")
image.draw()
print("Loading Image")
toGray(image)
