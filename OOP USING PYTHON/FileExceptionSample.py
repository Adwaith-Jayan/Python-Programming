try:
    f=open("text1.txt","w")
    f.write("Hello Good\nMorning")
except EOFError:
    f.close()
except IOError:
    f.close()
finally:
    f.close()