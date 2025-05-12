f=open("numbers.txt","r")
line=f.readline()
sum=0
while(line):
    try:
        num=int(line)
        sum+=num
    except ValueError:
        pass
    line=f.readline()
print(sum)
f.close()