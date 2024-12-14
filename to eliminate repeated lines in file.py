# WAP to eliminate repeated lines in file

f = open("rp.txt", "r")
data = f.readlines()
print("".join(set(data)))
