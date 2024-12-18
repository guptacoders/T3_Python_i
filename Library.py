# WAP using OOP Create a Class Library in which we can add books and display books 
# Books have attribute: bookname,booktitle,bookauthor & publisher name

class Library:
    def __init__(self, bname, btitle, bauthor, pubname):
        self.bname = bname
        self.btitle = btitle
        self.bauthor = bauthor
        self.pubname = pubname

    def display(self):
        # Display the book details
        print("Book Name: ", self.bname)
        print("Book Title: ", self.btitle)
        print("Author: ", self.bauthor)
        print("Publisher: ", self.pubname)

def store_book(book_list):
    # Take user input to create a new book and add it to the list
    bn = input("Enter Book Name: ")
    bt = input("Enter Book Title: ")
    ba = input("Enter Book Author: ")
    pn = input("Enter Publisher Name: ")
    
    # Create a book object and append it to the list
    book = Library(bn, bt, ba, pn)
    book_list.append(book)

    # Write the book data to the file
    with open("books.txt", "a") as f:
        f.write(f"Book Name: {bn}\n")
        f.write(f"Book Title: {bt}\n")
        f.write(f"Author: {ba}\n")
        f.write(f"Publisher: {pn}\n")
        f.write("-" * 40 + "\n")

def display_books(book_list):
    # Display all books in the list
    if book_list:
        for book in book_list:
            book.display()
            print("-" * 40)
    else:
        print("No books found!")

def main():
    book_list = []  # List to store book objects
    while True:
        choice = input("Do you want to (1) Store a new book or (2) Display all books or (3) Exit: ")
        if choice == '1':
            store_book(book_list)
        elif choice == '2':
            display_books(book_list)
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice, please try again.")

# Call the main function to start the program
main()
