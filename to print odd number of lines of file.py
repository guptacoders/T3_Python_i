# WAP to print odd number of lines of file 
   
with open('days.txt', 'r') as file:
    line_number = 1
    
    for line in file:
        if line_number % 2 != 0:
            print(line, end='') 
        line_number += 1
