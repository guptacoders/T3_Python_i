# WAP to remove '#' sign from the text 
f=open("file1.txt")
while(True):
    d=f.readline()
    if len(d)!=0:
        if d[0]=="#":
            continue
        else:
            if "#" in d:
                for i in range(1,len(d)):
                    if d[i]=="#":
                        print(d[0:i])
            else:
                print(d)
    else:
        break
