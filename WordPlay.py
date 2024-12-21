# Write a class called WordPlay. It should have a constructor that holds a list of words. The user of the class should pass the 
# list of words through constructor, which user wants to use for the class. The class should have following methods:
# 	words_with_length(length) — returns a list of all the words of length length
# 	starts_with(char1) — returns a list of all the words that start with char1
# 	ends_with(char2) — returns a list of all the words that end with char2
# 	palindromes() — returns a list of all the palindromes in the list
# 	only(str1) — returns a list of the words that contain only those letters in str1
# 	avoids(str2) — returns a list of the words that contain none of the letters in str2
# Make Required object for WordPlay class and test all the methods.
# For Example:
# If input list entered by user is: ['apple', 'banana', 'find', 'dictionary', 'set', 'tuple', 'list', 'malayalam', 'nayan', 'grind', 'apricot']
# words_with_length (5) should return ['apple', 'tuple', 'nayan', 'grind']
# starts_with ('a') should return ['apple', 'apricot']
# ends_with ('d') should return ['find', 'grind']
# palindromes () should return ['malayalam', 'nayan']
# only ('bna') should return ['banana']
# avoids ('amkd') should return ['set', 'tuple', 'list']

class Wordplay:
    def __init__(self):
        self.L=['apple', 'banana', 'find', 'dictionary', 'set', 'tuple', 'list', 'malayalam', 'nayan', 'grind', 'apricot']
    def only_s(self,s):
        s=set(s)
        l=[]
        for i in self.L:
            w=set(i)
            if s==w:
                l.append(i)
        print(l)

    def avoid(self,s):
        s=set(s)
        l=[]
        for i in self.L:
            w=set(i)
            if w.intersection(s)==set():
                l.append(i)
        print(l)

obj=Wordplay()
obj.only_s('ban')
obj.avoid('amkd')
