import json

# Define the file where the book library will be stored
library_file = "library.txt"

def load_library(fileName):
    """Load the library from a file. If the file doesn't exist or is empty, return an empty list."""
    try:
        with open(fileName, "r") as file:
            return json.load(file)  # Load book data from the file
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        return []  # Return an empty list if the file is missing or has invalid content

def save_books(fileName, books):
    """Save the current book list to the file."""
    with open(fileName, "w") as file:
        json.dump(books, file, indent=4)  # Save data in a readable JSON format

def display_menu():
    """Show the main menu with available options."""
    print("\n📚 Welcome to your Personal Library Manager!\n")
    print("1. Add a book")
    print("2. Remove a book")
    print("3. Search for a book")
    print("4. Display all books")
    print("5. Display statistics")
    print("6. Exit")

def add_book(all_books: list):
    """Allow the user to add a new book to the library."""
    title = input("Enter Title: ").strip()
    author = input("Enter Author: ").strip()

    # Ensure the user enters a valid publication year
    while True:
        try:
            year = int(input("Enter Publication Year: ").strip())
            break  # Exit loop if a valid year is entered
        except ValueError:
            print("❌ Invalid Input. Please enter a valid year.")

    genre = input("Enter Genre: ").strip()
    read_status = input("Have you read this book? (yes/no): ").strip().lower() == "yes"

    # Create a new book entry
    new_book = {
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "read": read_status
    }

    all_books.append(new_book)  # Add book to the list
    save_books(library_file, all_books)  # Save updated book list

    print("\n✅ Book added successfully!\n")

def remove_book(all_books: list):
    """Remove a book from the library by title."""
    book_to_remove = input("Enter the title of the book to remove: ").strip().lower()

    # Search for the book and remove it if found
    for single_book in all_books:
        if single_book["title"].lower() == book_to_remove:
            all_books.remove(single_book)
            save_books(library_file, all_books)  # Save updated book list
            print(f"✅ Book '{book_to_remove}' removed successfully!")
            break  # Stop searching after removing the book
    else:
        print("❌ Book not found.")  # This runs only if no book was removed

def search_book(all_books):
    """Search for a book by title or author."""
    print("🔍 Search by: \n1. Title\n2. Author")
    user_choice = input("Enter your choice (1/2): ").strip()

    if user_choice == "1":
        search_title = input("Enter the title: ").strip().lower()
        results = [book for book in all_books if book["title"].lower() == search_title]
    elif user_choice == "2":
        search_author = input("Enter the author: ").strip().lower()
        results = [book for book in all_books if book["author"].lower() == search_author]
    else:
        print("❌ Invalid choice.")
        return

    # Display search results
    if results:
        print("\n📚 Matching Books:")
        for index, book in enumerate(results, start=1):
            read_status = "Read" if book["read"] else "Unread"
            print(f"{index}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {read_status}")
    else:
        print("❌ No matching books found.")

def display_books(all_books):
    """Display all books in the library."""
    if not all_books:
        print("📚 Your library is empty.")
        return
    
    print("\n📚 Your Library:")
    for index, single_book in enumerate(all_books, start=1):
        read_status = "Read" if single_book["read"] else "Unread"
        print(f"{index}. {single_book['title']} by {single_book['author']} ({single_book['year']}) - {single_book['genre']} - {read_status}")

def display_statistics(all_books):
    """Show statistics about the user's library."""
    total_books = len(all_books)
    read_books = sum(1 for book in all_books if book["read"])

    if total_books == 0:
        print("📊 No books in your library.")
        return

    read_percentage = (read_books / total_books) * 100

    print("\n📊 Library Statistics:")
    print(f"📚 Total books: {total_books}")
    print(f"📖 Percentage read: {read_percentage:.2f}%")

def main():
    """Main function to run the library manager."""
    all_books: list = load_library(library_file)  # Load books from the file
    
    while True:
        display_menu()
        choice = input("Enter Choice (1-6): ").strip()

        if choice == "1":
            add_book(all_books)
        elif choice == "2":
            remove_book(all_books)
        elif choice == "3":
            search_book(all_books)
        elif choice == "4":
            display_books(all_books)
        elif choice == "5":
            display_statistics(all_books)
        elif choice == "6":
            print("📁 Library saved. Goodbye! 👋")
            break  # Exit the program
        else:
            print("❌ Invalid choice, please try again.")

if __name__ == "__main__":
    main()