# ================================================
# MINI LIBRARY MANAGEMENT SYSTEM
# ================================================
# Author: Paul Kizz
# Course: PROG211 (Object-Oriented Programming 1)
# ================================================

# -------- DATA STRUCTURES --------

books = {
    "9781234567890": {
        "title": "Python Programming",
        "author": "John Doe",
        "genre": "Non-Fiction",
        "total_copies": 3
    },
    "9780987654321": {
        "title": "Data Structures and Algorithms",
        "author": "Jane Smith",
        "genre": "Science",
        "total_copies": 5
    }
}

members = [
    {"member_id": "M001", "name": "Alice", "email": "alice@gmail.com", "borrowed_books": []},
    {"member_id": "M002", "name": "Bob", "email": "bob@gmail.com", "borrowed_books": ["9781234567890"]}
]

genres = ("Fiction", "Non-Fiction", "Science", "Romance", "Fantasy", "History")


# -------- CORE FUNCTIONS --------

def add_book(isbn, title, author, genre, total_copies):
    if isbn not in books and genre in genres:
        books[isbn] = {
            "title": title,
            "author": author,
            "genre": genre,
            "total_copies": total_copies
        }
        print(f"\n✅ Book '{title}' added successfully.")
    else:
        print("\n❌ Error: ISBN already exists or invalid genre.")


def add_member(member_id, name, email):
    for member in members:
        if member["member_id"] == member_id:
            print("\n❌ Error: Member ID already exists.")
            return
    members.append({"member_id": member_id, "name": name, "email": email, "borrowed_books": []})
    print(f"\n✅ Member '{name}' added successfully.")


def search_books(keyword):
    results = [book for book in books.values()
               if keyword.lower() in book["title"].lower()
               or keyword.lower() in book["author"].lower()]
    if results:
        print("\n🔍 Search Results:")
        for book in results:
            print(f" - {book['title']} by {book['author']} ({book['genre']})")
    else:
        print("\n⚠️ No books found.")


def update_book(isbn, title=None, author=None, genre=None, total_copies=None):
    if isbn in books:
        if title:
            books[isbn]["title"] = title
        if author:
            books[isbn]["author"] = author
        if genre and genre in genres:
            books[isbn]["genre"] = genre
        if total_copies is not None:
            books[isbn]["total_copies"] = total_copies
        print("\n✅ Book details updated successfully.")
    else:
        print("\n❌ Error: Book not found.")


def delete_book(isbn):
    if isbn in books:
        del books[isbn]
        print("\n🗑️ Book deleted successfully.")
    else:
        print("\n❌ Error: Book not found.")


def borrow_book(member_id, isbn):
    for member in members:
        if member["member_id"] == member_id:
            if len(member["borrowed_books"]) < 3 and isbn in books:
                member["borrowed_books"].append(isbn)
                print(f"\n📚 {member['name']} borrowed '{books[isbn]['title']}'.")
            else:
                print("\n⚠️ Cannot borrow: limit reached or book unavailable.")
            return
    print("\n❌ Error: Member not found.")


def return_book(member_id, isbn):
    for member in members:
        if member["member_id"] == member_id:
            if isbn in member["borrowed_books"]:
                member["borrowed_books"].remove(isbn)
                print(f"\n✅ {member['name']} returned '{books[isbn]['title']}'.")
            else:
                print("\n⚠️ Error: Book not in borrowed list.")
            return
    print("\n❌ Error: Member not found.")


def display_menu():
    print("\n========== MINI LIBRARY MANAGEMENT SYSTEM ==========")
    print("1. Add Book")
    print("2. Add Member")
    print("3. Search Book")
    print("4. Update Book")
    print("5. Delete Book")
    print("6. Borrow Book")
    print("7. Return Book")
    print("8. View All Books")
    print("9. Exit")
    print("====================================================")


def view_all_books():
    if books:
        print("\n📚 Library Books:")
        for isbn, details in books.items():
            print(f"- ISBN: {isbn}, Title: {details['title']}, Author: {details['author']}, Genre: {details['genre']}, Copies: {details['total_copies']}")
    else:
        print("\n⚠️ No books available.")


def main():
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-9): ")

        if choice == "1":
            isbn = input("Enter ISBN: ")
            title = input("Enter Title: ")
            author = input("Enter Author: ")
            genre = input(f"Enter Genre {genres}: ")
            total_copies = int(input("Enter Total Copies: "))
            add_book(isbn, title, author, genre, total_copies)

        elif choice == "2":
            member_id = input("Enter Member ID: ")
            name = input("Enter Name: ")
            email = input("Enter Email: ")
            add_member(member_id, name, email)

        elif choice == "3":
            keyword = input("Enter keyword to search (title/author): ")
            search_books(keyword)

        elif choice == "4":
            isbn = input("Enter ISBN to update: ")
            title = input("New Title (press enter to skip): ")
            author = input("New Author (press enter to skip): ")
            genre = input(f"New Genre {genres} (press enter to skip): ")
            total_copies = input("New Total Copies (press enter to skip): ")
            update_book(isbn, title or None, author or None, genre or None,
                        int(total_copies) if total_copies else None)

        elif choice == "5":
            isbn = input("Enter ISBN to delete: ")
            delete_book(isbn)

        elif choice == "6":
            member_id = input("Enter Member ID: ")
            isbn = input("Enter ISBN to borrow: ")
            borrow_book(member_id, isbn)

        elif choice == "7":
            member_id = input("Enter Member ID: ")
            isbn = input("Enter ISBN to return: ")
            return_book(member_id, isbn)

        elif choice == "8":
            view_all_books()

        elif choice == "9":
            print("\n👋 Exiting system... Goodbye!")
            break

        else:
            print("\n⚠️ Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
