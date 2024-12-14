# Make Name First Letter Capital and add area code in front of mobile number from student.txt file
# e.x:  i/p: walter melon melon@email.msmary.edu 447-3141
# o/p: Walter Melon melon@email.msmary.edu 330-447-3141

f=open("student.txt","r")
data=f.readlines()
for d in data:
    sp=d.split(' ')
    sp[0]=sp[0].title()
    sp[1]=sp[1].title()
    sp[3]="303-"+sp[3]
    w=' '.join(sp)
    print(w)
