class Book:

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def show_info(self):
        print("Book Name:", self.title)
        print("Author:", self.author)

        if self.is_borrowed:
            print("Status: Borrowed")
        else:
            print("Status: Available")

        print("-------------------")

    def borrow_book(self):

        if self.is_borrowed:
            print(self.title, "is already borrowed")
        else:
            self.is_borrowed = True
            print("You borrowed", self.title)

    def return_book(self):

        if self.is_borrowed:
            self.is_borrowed = False
            print("You returned", self.title)
        else:
            print(self.title, "was not borrowed")


# create objects
book1 = Book("Python Basics", "Ali Ahmadi")
book2 = Book("Clean Code", "Robert Martin")


# show information
book1.show_info()
book2.show_info()


# borrow a book
book1.borrow_book()

print()

# show information again
book1.show_info()


# return book
book1.return_book()

print()

# final info
book1.show_info()