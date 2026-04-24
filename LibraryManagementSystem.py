
class library:
    def __init__(self):
        self.books = {} 

    def add_book(self,book,author):
        self.books[book] = author
        print(f'\nTitle:{book} | Writer:{author}\n\tadded to the library.')
    
    def available_books(self):
        if self.books:
            print("\nBooks available in the library:")
            for book, author in self.books.items():
                print(f"Title: {book} | Writer: {author}")
        else:
            print('No books are currently available.')
        
    def lend_book(self,book_name,borrower,author):
        if book_name in self.books:
            print(f'\nBook:{book_name} | Writer:{author}\n\tis borrowed by {borrower}.')
            del self.books[book_name]
        else:
            print('\nThis book is not currently available.')

    def return_book(self,book_name,name,author):
        self.books[book_name] = author
        print(f'\nTitle:{book_name} by Author:{author}\n\tis returned to library by {name}.')
       
def main():
    my_library = library()

    while True:
        
        print('\n***** YK Library Management System *****.')
        print('Enter 0 to exit.')
        print('Enter 1 to add book.')
        print('Enter 2 to view available books.')
        print('Press 3 to lend a book.')
        print('Enter 4 to return a book.')
        choice = int(input('Enter you choice:'))

        if choice == 0:
            print('\nThanks for visiting YK Library.')
            break

        elif choice == 1:
            book = (input('Enter the name of the book to add:')).title()
            author = (input('Enter the name of the author:')).title()
            my_library.add_book(book,author)
        
        elif choice == 2:
            my_library.available_books()
        
        elif choice == 3:
            book_name = (input('Enter the name of the book which you want to lend:')).title()
            author = input('Enter name of the author:').title()
            borrower = (input('Enter your name:')).title()
            my_library.lend_book(book_name,borrower,author)
        
        elif choice == 4:
            book_name = (input('Enter the name of the book to return:')).title()
            author = (input('Enter the name of the author:')).title()
            name = (input('Enter your name:')).title()
            my_library.return_book(book_name,name,author)
        
        else:
            print('Invalid choice.')
        
if __name__ == '__main__':
    main()

