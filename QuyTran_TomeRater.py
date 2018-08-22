class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}
    
    def get_email(self):
        return self.email

    def change_email(self, address):
        self.email = address
        print("The user {} has been updated his/her email to {}!".format(self.name, self.email))

    def __repr__(self):
        return "User {u}, email address: {e}".format(u = self.name, e = self.email) 

    def __eq__(self, other_user):
        if self.name == other_user.name and self.email == other_user.email:
            return True
        else:
            return False

    def read_book(self, book, rating = None):
        self.rate = rating
        user = User(self.name, self.email)
        if self.rate != None:
            user.books[book] = self.rate

    def get_average_rating(self):
        count = 0
        rating_sum = 0    
        for value in self.books.values():
            if type(value) == int:
                rating_sum += value
            count += 1
        return rating_sum / count


class Book:
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []
    
    def __repr__(self):
        return "The book with title {} and isbn = {}".format(self.title, self.isbn)
    
    def get_title(self):
        return self.title
    
    def get_isbn(self):
        return self.isbn
    
    def set_isbn(self, new_isbn):
        self.isbn = new_isbn
        print("This book's isbn has been updated to {}".format(self.isbn))
        
    def add_rating(self, rating):
        self.rating = rating
        if type(self.rating) == int:
            if self.rating >= 0 and self.rating <= 4:
                self.ratings += [self.rating]
            else:
                print("Invalid Rating")
            
    def __eq__(self, other_book):
        if self.title == other_book.title and self.isbn == other_book.isbn:
            return True
        else:
            return False
        
    def get_average_rating(self):
        count = 0
        rating_sum = 0
        for value in self.ratings:
            count += 1
            rating_sum += value
        return rating_sum / count
    
    def __hash__(self):
        return hash((self.title, self.isbn))  

    
class Fiction(Book):
    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = author

    def get_author(self):
        return self.author

    def __repr__(self):
        return "{title} by {author}".format(title = self.title, author = self.author)


class Non_Fiction(Book):
    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        self.subject = subject
        self.level = level

    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level

    def __repr__(self):
        return "{title}, a {level} manual on {subject}".format(title = self.title, level = self.level, subject = self.subject)


class TomeRater:
    def __init__(self):
        self.users = {}
        self.books = {}

    def create_book(self, title, isbn):
        self.book_object = Book(title, isbn)
        return self.book_object
        
    def create_novel(self, title, author, isbn):
        self.novel_object = Fiction(title, author, isbn)
        return self.novel_object
          
    def create_non_fiction(self, title, subject, level, isbn):
        self.nonfiction_object = Non_Fiction(title, subject, level, isbn)
        return self.nonfiction_object
    
    def add_book_to_user(self, book, email, rating = None):
        self.email = email
        self.book = book
        self.rate = rating
        if self.email not in self.users:
            print("No user with email {email}!".format(email = self.email))
        else:
            self.user_object = self.users[self.email]
            self.user_object.read_book(self.book, self.rate)
            self.user_object.books[self.book] = self.rate
            for book in self.user_object.books:
                if book == self.book:
                    book.add_rating(self.rate)        
            if self.book not in self.books:
                self.books[self.book] = 1
            else:
                self.books[self.book] += 1
                
    def add_user(self, name, email, user_books = None):
        self.name = name
        self.email = email
        self.user_books = user_books
        new_user_object = User(self.name, self.email)
        self.users[self.email] = new_user_object
        if self.user_books != None:
            for user_book in self.user_books:
                self.add_book_to_user(user_book, self.email)
        
                
    def print_catalog(self):
        for key in self.books:
            print(key)
    
    def print_users(self):
        for value in self.users.values():
            print(value)
            
    def most_read_book(self):
        max_rate = 0
        most_read_book = 0
        for key, value in self.books.items():
            if value > max_rate:
                max_rate = value
                most_read_book = key
        return most_read_book
    
    def highest_rated_book(self):
        highest_average_rating = 0
        highest_rated_book = 0
        for book in self.books.keys():
            average_rating = book.get_average_rating()
            if average_rating > highest_average_rating:
                highest_average_rating = average_rating
                highest_rated_book = book
        return highest_rated_book
    
    def most_positive_user(self):
        highest_average_rating = 0
        most_positive_user = 0
        for value in self.users.values():
            if value.get_average_rating() > highest_average_rating:
                highest_average_rating = value.get_average_rating()
                most_positive_user = value
        return most_positive_user
                
                
            

