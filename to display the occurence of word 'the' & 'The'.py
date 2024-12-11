# WAP to display the occurence of word 'the' & 'The'

count=0
f=open("story.txt")
data=f.read()
s=data.split(" ")
for i in s:
    if(i=="the" or i=="The"):
        count+=1
print(count)
