#WAP TO  READ MBOX-SHORT.TXT FIND A LINE THAT STARTWITH 'FROM' AND LIST OUT EMAIL ID 
count=0
max_count=0
max_email=""
f=open("mbox-short.txt","r")
data=f.readlines()
for i in data:
    if i.startswith("From:"):
        words=i.split()
        count+=1
        print(words[1])
        
    if count>max_count:
        max_count=count
        max_email=words
        
# print("Total Emails: ",count)
# print(max_email)
print(f"The Most Repetative Email is : {max_email} with {max_count} Occurence.")
