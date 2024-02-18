import os
class Library:
    def __init__(self):
        global file
        # Open the file in append mode for reading and writing
        self.file = open("books.txt", "a+", encoding="utf-8")
        
    def ana_menu(self):
        while True:
            os.system("cls") # Clear the screen
            print("\nMENU\n")
            print("1- List Books \n")
            print("2- Add Books\n")
            print("3- Remove Book\n")
            print("Press 'q' to quit\n")
            choice = input("Choice: ")
            
            if (choice == "1"):
                self.list_book()

            elif(choice == "2"):
                self.add_book()
                
            elif(choice == "3"):
                self.remove_book()

            elif(choice.lower() == "q"):
                break

            else:
                print("Enter valid value!!")
                os.system("pause")
                
    def add_book(self):

        # Get input for the new book
        book_name = input("Book's name:").title()
        book_author = input("Book's auther:").title()
        release_year = input("Book's release year:").title()
        book_pages = input("Book's page:").title()

        # Check if the book already exists
        self.file.seek(0)
        lines = self.file.readlines()
        book_exists = False
        for line in lines:
            if line.startswith(f"Book Name: {book_name}"):
                book_exists = True                

        if book_exists:
            print("Book already exists.")
            os.system("pause")
        else:    
            # Add the new book to the file
            self.file.write(f"Book Name: {book_name} , Book Author: {book_author} , Release Year: {release_year} , Number of Pages: {book_pages}\n")        
        
    def list_book(self):
        # List all the books in the file
        self.file.seek(0)
        books = self.file.read().splitlines(True)
        for book in books:
            books_list = book.split(",")
            print(books_list[0] + " - " + books_list[1])
        os.system("pause")

    def remove_book(self):
        # Remove a book from the file
        self.file.seek(0)
        books = self.file.readlines()        
        book_name = input("Enter the book name:").title()
        new_books = []
        removed = False
        for book in books:
            if book.startswith(f"Book Name: {book_name}"):
                removed = True
                
            else: 
                new_books.append(book)

        if removed:
            # Update the file with the remaining books
            self.file.seek(0)
            self.file.truncate()
            self.file.seek(0)
            for book in new_books:
                self.file.write(book)
            print("Book removed successfully.")
            os.system("pause")
        else:
            print("Book not found.")
            os.system("pause")
        
    
    def __del__(self):
        # Close the file when the object is deleted
        self.file.close()

# Create a Library object and start the menu
lib = Library()
lib.ana_menu()