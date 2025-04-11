from images import Image

def toBlackAndWhite(image):
    print("Loading image")
    black_pixel=(0,0,0)
    white_pixel=(255,255,255)
    for y in range(image.getHeight()):
        for x in range(image.getWidth()):
            r,g,b=image.getPixel(x,y)
            average=r+g+b//3
            if average <127:
                image.setPixel(x,y,black_pixel)
            else:
                image.setPixel(x,y,white_pixel)
    print("Close window to exit")
    image.draw()



file=input("Enter filename of image: ")
image=Image(file)
print("Close window to continue")
image.draw()
toBlackAndWhite(image)