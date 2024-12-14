# WAP to reverse a line given by user and print whole data with that reversed line


f = open("frd.txt", "r")
data = f.readlines() 

ln = int(input("Enter Line number: "))

w = data[ln - 1].split()
a = w[::-1]  
data[ln - 1] = " ".join(a)+"\n" 

for line in data:
    print(line, end="") 
