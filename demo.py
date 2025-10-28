# demo.py - Library Management System Demo Script

from operations import *

print("=" * 60)
print("LIBRARY MANAGEMENT SYSTEM DEMONSTRATION")
print("=" * 60)

# 1. ADDING BOOKS
print("\n1. ADDING BOOKS TO LIBRARY")
print("-" * 40)
print(add_book("978-0-7475-3269-9", "Harry Potter and the Philosopher's Stone", "J.K. Rowling", "Fiction", 5))
print(add_book("978-0-590-35340-3", "Harry Potter and the Chamber of Secrets", "J.K. Rowling", "Fiction", 3))
print(add_book("978-0-06-112008-4", "To Kill a Mockingbird", "Harper Lee", "Fiction", 4))
print(add_book("978-0-553-29337-9", "A Brief History of Time", "Stephen Hawking", "Non-Fiction", 2))
print(add_book("978-0-7653-7698-5", "The Martian", "Andy Weir", "Sci-Fi", 3))

# Display all books
display_all_books()

# 2. ADDING MEMBERS
print("\n2. ADDING MEMBERS")
print("-" * 40)
print(add_member("M001", "John Doe", "john.doe@email.com", "123-456-7890"))
print(add_member("M002", "Jane Smith", "jane.smith@email.com", "098-765-4321"))
print(add_member("M003", "Alice Johnson", "alice.j@email.com", "555-123-4567"))

# Display all members
display_all_members()

# 3. SEARCHING BOOKS
print("\n3. SEARCHING FOR BOOKS")
print("-" * 40)
print("Searching for 'Harry Potter':")
results = search_books("Harry Potter")
for book in results:
    print(f"  - {book['title']} by {book['author']}")

print("\nSearching for author 'Stephen Hawking':")
results = search_books("Stephen Hawking")
for book in results:
    print(f"  - {book['title']} by {book['author']}")

# 4. BORROWING BOOKS
print("\n4. BORROWING BOOKS")
print("-" * 40)
print(borrow_book("M001", "978-0-7475-3269-9"))  # John borrows Harry Potter 1
print(borrow_book("M001", "978-0-590-35340-3"))  # John borrows Harry Potter 2
print(borrow_book("M002", "978-0-06-112008-4"))  # Jane borrows To Kill a Mockingbird
print(borrow_book("M002", "978-0-553-29337-9"))  # Jane borrows Brief History
print(borrow_book("M003", "978-0-7653-7698-5"))  # Alice borrows The Martian

# Display updated books status
display_all_books()

# 5. TESTING BORROW LIMIT
print("\n5. TESTING BORROW LIMIT (Max 3 books)")
print("-" * 40)
print(borrow_book("M001", "978-0-7653-7698-5"))  # John tries to borrow 3rd book
print(borrow_book("M001", "978-0-06-112008-4"))  # John tries to borrow 4th book (should fail)

# 6. RETURNING BOOKS
print("\n6. RETURNING BOOKS")
print("-" * 40)
print(return_book("M001", "978-0-7475-3269-9"))  # John returns Harry Potter 1
print(return_book("M002", "978-0-553-29337-9"))  # Jane returns Brief History

# Display updated books status
display_all_books()

# 7. UPDATING BOOK DETAILS
print("\n7. UPDATING BOOK INFORMATION")
print("-" * 40)
print(update_book("978-0-7475-3269-9", total_copies=6))
print(update_book("978-0-553-29337-9", author="Stephen W. Hawking"))

# Display updated books
display_all_books()

# 8. UPDATING MEMBER DETAILS
print("\n8. UPDATING MEMBER INFORMATION")
print("-" * 40)
print(update_member("M001", email="john.newemail@email.com", contact="111-222-3333"))

# Display updated members
display_all_members()

# 9. TESTING DELETE WITH BORROWED BOOKS
print("\n9. TESTING DELETE RESTRICTIONS")
print("-" * 40)
print("Trying to delete book with borrowed copies:")
print(delete_book("978-0-590-35340-3"))  # Should fail - John still has it

print("\nTrying to delete member with borrowed books:")
print(delete_member("M001"))  # Should fail - John still has books

# 10. SUCCESSFUL DELETION
print("\n10. SUCCESSFUL DELETION (After returning)")
print("-" * 40)
print(return_book("M001", "978-0-590-35340-3"))  # John returns last book
print(return_book("M001", "978-0-7653-7698-5"))  # John returns last book
print("\nNow deleting member M001:")
print(delete_member("M001"))  # Should succeed now

print("\nDeleting book with no borrowed copies:")
print(delete_book("978-0-7653-7698-5"))  # Should succeed

# Final status
print("\n" + "=" * 60)
print("FINAL LIBRARY STATUS")
print("=" * 60)
display_all_books()
display_all_members()

print("\n" + "=" * 60)
print("DEMONSTRATION COMPLETE")
print("=" * 60)