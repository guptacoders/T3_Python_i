# WAP to compare 2 files give the line and column number from where the first difference occurence 

f1 = open("file1.txt")
f2 = open("file2.txt")
d1 = f1.readlines()
d2 = f2.readlines()

for i,j in enumerate(d1):  
    if j != d2[i]:
        for ind, char in enumerate(j):
            if char != d2[i][ind]:
                print("line no =", i + 1)  
                print("index no =", ind)  
                break
    break

f1.close()
f2.close()
