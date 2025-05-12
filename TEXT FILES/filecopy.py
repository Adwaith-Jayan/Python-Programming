f=open("input.txt","rb")
f2=open("output.txt","wb")
line=f.readline()
while line:
    f2.write(line)
    line=f.readline()
f.close()
f2.close()