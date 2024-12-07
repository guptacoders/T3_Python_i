# WAP to create "days.txt" file Write all 7 days into file. Print the data of file into console.
# Count the number of lines 

f=open("days.txt","w")
l=["Monday\n","Tuesday\n","Wednesday\n","Thursday\n","Friday\n","Saturday\n","Sunday"]
f.writelines(l)
f.close()

count=0
with open("days.txt","r") as f:
    d=f.read()
    print(d)
    
f=open("days.txt","r")
c=0
for i in f:
    c+=1
print("No of lines:",c)
