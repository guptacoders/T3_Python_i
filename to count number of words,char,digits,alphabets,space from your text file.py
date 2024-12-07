# WAP to count number of words,char,digits,alphabets,space from your text file
f=open("words.txt","a")

data = """Hello, this is a sample text file.
It contains words, digits like 123, and some special characters!
Let's count alphabets, digits, spaces, etc.
"""

f.write(data)
f.close()

f = open("words.txt", "r")

word_count = 0
char_count = 0
digit_count = 0
alphabet_count = 0
space_count = 0

content = f.read()

for char in content:
    char_count += 1
    if char.isdigit():
        digit_count += 1 
    elif char.isalpha():
        alphabet_count += 1  
    elif char == " ":
        space_count += 1 

word_count = len(content.split())

f.close()

print("Words:", word_count)
print("Characters:", char_count)
print("Digits:", digit_count)
print("Alphabets:", alphabet_count)
print("Spaces:", space_count)
