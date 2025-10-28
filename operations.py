# operations.py - Library Management System Core Functions

# Data Structures
books = []  # List to store book dictionaries
members = []  # List to store member dictionaries
VALID_GENRES = ("Fiction", "Non-Fiction", "Sci-Fi")  # Tuple of valid genres


# ===== BOOK OPERATIONS =====

def add_book(isbn, title, author, genre, total_copies):
    """Add a new book to the library system"""
    # Check if ISBN is unique
    for book in books:
        if book["isbn"] == isbn:
            return "Error: ISBN already exists"

    # Check if genre is valid
    if genre not in VALID_GENRES:
        return f"Error: Genre must be one of {VALID_GENRES}"

    # Create book dictionary
    new_book = {
        "isbn": isbn,
        "title": title,
        "author": author,
        "genre": genre,
        "total_copies": total_copies,
        "available_copies": total_copies
    }

    books.append(new_book)
    return f"Book '{title}' added successfully"


def search_books(search_term):
    """Search books by title or author"""
    results = []
    search_lower = search_term.lower()

    for book in books:
        if search_lower in book["title"].lower() or search_lower in book["author"].lower():
            results.append(book)

    return results


def update_book(isbn, title=None, author=None, genre=None, total_copies=None):
    """Update book details"""
    for book in books:
        if book["isbn"] == isbn:
            if title:
                book["title"] = title
            if author:
                book["author"] = author
            if genre:
                if genre in VALID_GENRES:
                    book["genre"] = genre
                else:
                    return f"Error: Genre must be one of {VALID_GENRES}"
            if total_copies is not None:
                book["total_copies"] = total_copies
            return f"Book with ISBN {isbn} updated successfully"

    return "Error: Book not found"


def delete_book(isbn):
    """Delete a book only if no copies are borrowed"""
    for book in books:
        if book["isbn"] == isbn:
            if book["available_copies"] < book["total_copies"]:
                return "Error: Cannot delete book with borrowed copies"
            books.remove(book)
            return f"Book with ISBN {isbn} deleted successfully"

    return "Error: Book not found"


# ===== MEMBER OPERATIONS =====

def add_member(member_id, name, email, contact):
    """Add a new member to the library system"""
    # Check if member ID is unique
    for member in members:
        if member["id"] == member_id:
            return "Error: Member ID already exists"

    # Create member dictionary
    new_member = {
        "id": member_id,
        "name": name,
        "email": email,
        "contact": contact,
        "borrowed_books": []  # List to track borrowed book ISBNs
    }

    members.append(new_member)
    return f"Member '{name}' added successfully"


def update_member(member_id, name=None, email=None, contact=None):
    """Update member details"""
    for member in members:
        if member["id"] == member_id:
            if name:
                member["name"] = name
            if email:
                member["email"] = email
            if contact:
                member["contact"] = contact
            return f"Member with ID {member_id} updated successfully"

    return "Error: Member not found"


def delete_member(member_id):
    """Delete a member only if they have no borrowed books"""
    for member in members:
        if member["id"] == member_id:
            if len(member["borrowed_books"]) > 0:
                return "Error: Cannot delete member with borrowed books"
            members.remove(member)
            return f"Member with ID {member_id} deleted successfully"

    return "Error: Member not found"


# ===== BORROW/RETURN OPERATIONS =====

def borrow_book(member_id, isbn):
    """Allow a member to borrow a book"""
    # Find member
    member = None
    for m in members:
        if m["id"] == member_id:
            member = m
            break

    if not member:
        return "Error: Member not found"

    # Check if member already has 3 books
    if len(member["borrowed_books"]) >= 3:
        return "Error: Member has already borrowed 3 books"

    # Find book
    book = None
    for b in books:
        if b["isbn"] == isbn:
            book = b
            break

    if not book:
        return "Error: Book not found"

    # Check if book is available
    if book["available_copies"] <= 0:
        return "Error: No copies available"

    # Borrow the book
    member["borrowed_books"].append(isbn)
    book["available_copies"] -= 1
    return f"Book '{book['title']}' borrowed successfully by {member['name']}"


def return_book(member_id, isbn):
    """Allow a member to return a borrowed book"""
    # Find member
    member = None
    for m in members:
        if m["id"] == member_id:
            member = m
            break

    if not member:
        return "Error: Member not found"

    # Check if member has borrowed this book
    if isbn not in member["borrowed_books"]:
        return "Error: Member has not borrowed this book"

    # Find book
    book = None
    for b in books:
        if b["isbn"] == isbn:
            book = b
            break

    if not book:
        return "Error: Book not found"

    # Return the book
    member["borrowed_books"].remove(isbn)
    book["available_copies"] += 1
    return f"Book '{book['title']}' returned successfully by {member['name']}"


# ===== DISPLAY FUNCTIONS =====

def display_all_books():
    """Display all books in the library"""
    if not books:
        return "No books in the library"

    print("\n=== ALL BOOKS ===")
    for book in books:
        print(f"ISBN: {book['isbn']}, Title: {book['title']}, Author: {book['author']}, "
              f"Genre: {book['genre']}, Available: {book['available_copies']}/{book['total_copies']}")
    return ""


def display_all_members():
    """Display all members"""
    if not members:
        return "No members registered"

    print("\n=== ALL MEMBERS ===")
    for member in members:
        print(f"ID: {member['id']}, Name: {member['name']}, Email: {member['email']}, "
              f"Borrowed Books: {len(member['borrowed_books'])}")
    return ""