# WAP to read mbox-short.txt Find a line which starts with 'From' and list out email ids 

f1 = open("mbox-short.txt", "r")
lines = f1.readlines()
count=0

for line in lines:
    if line.startswith("From:"):
        words = line.split()
        count+=1
        print(words[1])
       
            
print("\nTotal Email Id's: ",count)
