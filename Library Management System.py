# Library Management System
# A menu-driven Python project using classes, objects, lists, dictionaries,
# functions, loops, and conditional statements.

class Book:
    """Represents a book in the library."""

    def __init__(self, book_id, title, author, quantity):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.quantity = quantity  # Number of copies currently available

    def display_info(self):
        print("Book ID:", self.book_id)
        print("Title:", self.title)
        print("Author:", self.author)
        print("Available Quantity:", self.quantity)


class Library:
    """Manages books and the records of issued books."""

    def __init__(self):
        self.books = {}          # Dictionary: book ID -> Book object
        self.issued_books = []   # List of dictionaries for issued copies

    def add_book(self, book_id, title, author, quantity):
        if book_id in self.books:
            print("A book with this ID already exists.")
            return

        if quantity <= 0:
            print("Quantity must be a positive whole number.")
            return

        new_book = Book(book_id, title, author, quantity)
        self.books[book_id] = new_book
        print("Book added successfully!")

    def view_all_books(self):
        if not self.books:
            print("No books are currently registered in the library.")
            return

        print("\n========== ALL BOOKS ==========")
        for book in self.books.values():
            print("------------------------------")
            book.display_info()
        print("==============================")

    def search_book(self, search_value):
        search_value = search_value.strip()
        found_books = []

        # First check whether the entered value is a book ID.
        if search_value in self.books:
            found_books.append(self.books[search_value])
        else:
            # Otherwise, search titles without considering letter case.
            for book in self.books.values():
                if search_value.lower() in book.title.lower():
                    found_books.append(book)

        if not found_books:
            print("No book found with that ID or title.")
            return

        print("\n========== SEARCH RESULTS ==========")
        for book in found_books:
            print("------------------------------")
            book.display_info()

    def issue_book(self, book_id, student_name):
        if book_id not in self.books:
            print("Book not found.")
            return

        book = self.books[book_id]

        if book.quantity <= 0:
            print("This book is currently unavailable.")
            return

        if not student_name.strip():
            print("Student name cannot be empty.")
            return

        # Reduce the available quantity by one.
        book.quantity -= 1

        # Save the issue details so the book can be returned later.
        issue_record = {
            "book_id": book_id,
            "title": book.title,
            "student_name": student_name.strip()
        }
        self.issued_books.append(issue_record)

        print("Book issued successfully!")
        print("Available Quantity:", book.quantity)

    def return_book(self, book_id, student_name):
        if book_id not in self.books:
            print("Book not found.")
            return

        if not student_name.strip():
            print("Student name cannot be empty.")
            return

        # Find a matching issue record for this book and student.
        for index, record in enumerate(self.issued_books):
            if (record["book_id"] == book_id and
                    record["student_name"].lower() == student_name.strip().lower()):

                self.issued_books.pop(index)
                self.books[book_id].quantity += 1

                print("Book returned successfully!")
                print("Available Quantity:", self.books[book_id].quantity)
                return

        print("No matching issued-book record was found for this student.")

    def delete_book(self, book_id):
        if book_id not in self.books:
            print("Book not found.")
            return

        # Do not delete a book if any copy is currently issued.
        for record in self.issued_books:
            if record["book_id"] == book_id:
                print("Cannot delete this book because a copy is currently issued.")
                return

        del self.books[book_id]
        print("Book deleted successfully!")

    def view_issued_books(self):
        if not self.issued_books:
            print("There are no books currently issued.")
            return

        print("\n========== ISSUED BOOKS ==========")
        for number, record in enumerate(self.issued_books, start=1):
            print("------------------------------")
            print("Issue Number:", number)
            print("Book ID:", record["book_id"])
            print("Book Title:", record["title"])
            print("Student Name:", record["student_name"])
        print("===============================")


def get_positive_integer(message):
    """Ask until the user enters a positive whole number."""
    while True:
        try:
            number = int(input(message))
            if number > 0:
                return number
            print("Please enter a number greater than zero.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def display_menu():
    """Display the main menu."""
    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Add Book")
    print("2. View All Books")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Delete Book")
    print("7. View Issued Books")
    print("8. Exit")


def main():
    library = Library()

    # Keep showing the menu until the user chooses Exit.
    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            print("\n========== ADD NEW BOOK ==========")
            book_id = input("Enter Book ID: ").strip()
            title = input("Enter Book Title: ").strip()
            author = input("Enter Author Name: ").strip()

            if not book_id or not title or not author:
                print("Book ID, title, and author cannot be empty.")
                continue

            quantity = get_positive_integer("Enter Quantity: ")
            library.add_book(book_id, title, author, quantity)

        elif choice == "2":
            library.view_all_books()

        elif choice == "3":
            print("\n========== SEARCH BOOK ==========")
            search_value = input("Enter Book ID or Title: ").strip()

            if not search_value:
                print("Please enter a book ID or title.")
            else:
                library.search_book(search_value)

        elif choice == "4":
            print("\n========== ISSUE BOOK ==========")
            book_id = input("Enter Book ID: ").strip()
            student_name = input("Enter Student Name: ").strip()
            library.issue_book(book_id, student_name)

        elif choice == "5":
            print("\n========== RETURN BOOK ==========")
            book_id = input("Enter Book ID: ").strip()
            student_name = input("Enter Student Name: ").strip()
            library.return_book(book_id, student_name)

        elif choice == "6":
            print("\n========== DELETE BOOK ==========")
            book_id = input("Enter Book ID: ").strip()
            library.delete_book(book_id)

        elif choice == "7":
            library.view_issued_books()

        elif choice == "8":
            print("Thank you for using the Library Management System!")
            print("Program closed successfully.")
            break

        else:
            print("Invalid choice. Please select a number from 1 to 8.")


# Start the program.
if __name__ == "__main__":
    main()
