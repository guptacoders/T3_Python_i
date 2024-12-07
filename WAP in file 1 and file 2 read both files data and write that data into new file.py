# WAP in file 1 and file 2 read both files data and write that data into new file

f1=open("file1.txt","a+")
f2=open("file2.txt","a+")
list=["1\n","2\n","3\n","4\n"]
f1.writelines(list)
list2=["A\n","B\n","C\n","D\n","E\n","F"]
f2.writelines(list2)

f3=open("file3.txt","a+")

f3.writelines(f1.readlines())
f3.writelines(f2.readlines())

f1.close()
f2.close()
f3.close()
