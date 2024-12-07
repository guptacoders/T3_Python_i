# WAP to ask a user name and age and write it in a file and print on console

f=open("details.txt","a")
name=input("Enter Name:")
age=input("Enter Age:")

f.write("\n")
f.write(name)
f.write("\n")
f.write(age)


with open("details.txt","r") as f:
    d=f.read()
    print(d)
    
