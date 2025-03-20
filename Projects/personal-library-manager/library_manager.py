import json

library_file = "library.txt"

def load_library(fileName):
    """Load the Library from file"""
    try:
        with open(fileName,"r") as file:
            return json.load(file)
    except (FileNotFoundError,json.decoder.JSONDecodeError):
        return []

def save_books(fileName,books):
    """Save the Library to file"""
    with open(fileName, "w") as file:
        json.dump(books, file, indent=4)

def display_menu():
    """Display the main menu."""
    print("\nWelcome to your Personal Library Manager!\n")
    print("1. Add a book")
    print("2. Remove a book")
    print("3. Search for a book")
    print("4. Display all books")
    print("5. Display statistics")
    print("6. Exit")

def add_book(all_books:list):
    """Add a new book to library."""
    title = input("Enter Title: ").strip()
    author = input("Enter Author: ").strip()
    while True:
        try:
            year = int(input("Enter Publication Year: ").strip())
            break
        except ValueError:
            print("Invalid Input. Please Enter a valid year.")
    genre = input("Enter Genre: ").strip()
    read_status = input("Have you read this book? (yes/no): ").strip() == True

    new_Book = {
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "read": read_status
    }
    all_books.append(new_Book)
    save_books(library_file,all_books)

    print("\nBook Added Successfully!\n")

def remove_book(all_books:list):
    """Remove a book from Library by title."""
    book_to_remove = input("Enter the title to of the book to remove: ").strip().lower()

    for single_book in all_books:
        if single_book["title"].lower() == book_to_remove:
            all_books.remove(single_book)
            save_books(library_file, all_books)
            print("Book Removed Successfully!")
            break # exit loop after removing book without extra iteration
    else:    
        print("Book not found") # if loop not break print block will execute

def search_book(all_books):
    print("Searching Book by title or author")

def display_books(all_books):
    if not all_books:
        print("📚 Your library is empty.")
        return
    
    print("\n📚 Your Library:")
    for index, single_book in enumerate(all_books,start=1):
        print(f"{index}. {single_book["title"]} by {single_book["author"]} ({single_book["year"]}) - {single_book["genre"]} - {"Read" if single_book["read"] else "Unread"}")

def display_statistics(all_books):
    total_books = len(all_books)
    read_books = sum(1 for single_book in all_books if single_book["read"])

    if total_books == 0:
        print("📊 No books in your library.")
        return
    read_percentage = (read_books / total_books) * 100

    print(f"\n📊 Total books: {total_books}")
    print(f"📖 Percentage read: {read_percentage:.2f}%")


def main():
    all_books:list = load_library(library_file)
    
    while True:
        display_menu()
        choice = input("Enter Choice (1-6): ")
        if choice == "1":
            add_book(all_books)
        elif choice == "2":
            remove_book(all_books)
        elif choice == "3":
            print("3. Search for a book")
        elif choice == "4":
            display_books(all_books)
        elif choice == "5":
            display_statistics(all_books)
        elif choice == "6":
            print("6. Exit")
            break
        else:
            print("\n Invalid Choice. Please Try Again. \n")


main()