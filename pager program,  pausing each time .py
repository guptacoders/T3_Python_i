# WAP a pager program your solution should prompt for file name and display the text file 25 lines at a time
# pausing each time to ask the user to press a key to continue or quit ?

fname = input("Enter File Name: ")
with open(fname) as f1:
    for i, j in enumerate(f1):
        if i % 25 == 0 and i: 
            x = input("Enter q to quit or press any key to continue: ")
            if x.lower() == "q": 
                break
        else:
            print(j, end='') 
