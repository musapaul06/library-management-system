# tests.py - Library Management System Unit Tests

from operations import *

print("=" * 60)
print("LIBRARY MANAGEMENT SYSTEM - UNIT TESTS")
print("=" * 60)

# Clear any existing data
books.clear()
members.clear()

# TEST 1: Adding books with unique ISBN
print("\nTEST 1: Add book with unique ISBN")
result = add_book("TEST-001", "Test Book 1", "Test Author", "Fiction", 5)
assert "added successfully" in result, "Failed to add book with unique ISBN"
assert len(books) == 1, "Book list should have 1 book"
print("✓ PASSED: Book added successfully with unique ISBN")

# TEST 2: Prevent duplicate ISBN
print("\nTEST 2: Prevent adding book with duplicate ISBN")
result = add_book("TEST-001", "Test Book 2", "Another Author", "Fiction", 3)
assert "Error" in result, "Should not allow duplicate ISBN"
assert len(books) == 1, "Book list should still have only 1 book"
print("✓ PASSED: Duplicate ISBN rejected")

# TEST 3: Validate genre using tuple
print("\nTEST 3: Validate genre from tuple")
result = add_book("TEST-002", "Test Book 3", "Test Author", "InvalidGenre", 2)
assert "Error" in result, "Should reject invalid genre"
assert len(books) == 1, "Invalid genre book should not be added"
print("✓ PASSED: Invalid genre rejected")

# TEST 4: Add member and enforce borrow limit (max 3 books)
print("\nTEST 4: Enforce maximum borrow limit (3 books)")
# Setup
add_member("TEST-M001", "Test Member", "test@email.com", "123-456")
add_book("TEST-003", "Book 2", "Author 2", "Fiction", 5)
add_book("TEST-004", "Book 3", "Author 3", "Sci-Fi", 5)
add_book("TEST-005", "Book 4", "Author 4", "Non-Fiction", 5)

# Borrow 3 books
borrow_book("TEST-M001", "TEST-001")
borrow_book("TEST-M001", "TEST-003")
borrow_book("TEST-M001", "TEST-004")

# Try to borrow 4th book
result = borrow_book("TEST-M001", "TEST-005")
assert "Error" in result and "3 books" in result, "Should prevent borrowing more than 3 books"

# Verify member has exactly 3 books
member = None
for m in members:
    if m["id"] == "TEST-M001":
        member = m
        break
assert len(member["borrowed_books"]) == 3, "Member should have exactly 3 borrowed books"
print("✓ PASSED: Borrow limit enforced (max 3 books)")

# TEST 5: Delete restrictions - cannot delete book with borrowed copies
print("\nTEST 5: Prevent deletion of book with borrowed copies")
result = delete_book("TEST-001")
assert "Error" in result and "borrowed" in result, "Should not allow deleting borrowed book"

# Find book and verify it still exists
book_exists = False
for book in books:
    if book["isbn"] == "TEST-001":
        book_exists = True
        break
assert book_exists, "Book should still exist after failed deletion"
print("✓ PASSED: Cannot delete book with borrowed copies")

# TEST 6: Delete restrictions - cannot delete member with borrowed books
print("\nTEST 6: Prevent deletion of member with borrowed books")
result = delete_member("TEST-M001")
assert "Error" in result and "borrowed" in result, "Should not allow deleting member with books"

# Verify member still exists
member_exists = False
for member in members:
    if member["id"] == "TEST-M001":
        member_exists = True
        break
assert member_exists, "Member should still exist after failed deletion"
print("✓ PASSED: Cannot delete member with borrowed books")

# TEST 7: Return book functionality
print("\nTEST 7: Return book updates availability")
# Get initial available copies
initial_copies = None
for book in books:
    if book["isbn"] == "TEST-001":
        initial_copies = book["available_copies"]
        break

return_book("TEST-M001", "TEST-001")

# Get updated available copies
updated_copies = None
for book in books:
    if book["isbn"] == "TEST-001":
        updated_copies = book["available_copies"]
        break

assert updated_copies == initial_copies + 1, "Available copies should increase by 1 after return"
print("✓ PASSED: Book return updates availability correctly")

# TEST 8: Search functionality (using lists and dictionaries)
print("\nTEST 8: Search books by title or author")
results = search_books("Test Book")
assert len(results) >= 1, "Should find books matching 'Test Book'"

results = search_books("Author 2")
assert len(results) == 1, "Should find exactly one book by 'Author 2'"
assert results[0]["isbn"] == "TEST-003", "Should find correct book"
print("✓ PASSED: Search functionality works correctly")

print("\n" + "=" * 60)
print("ALL TESTS PASSED SUCCESSFULLY!")
print("=" * 60)
print("\nTest Summary:")
print("✓ Test 1: Unique ISBN validation")
print("✓ Test 2: Duplicate ISBN prevention")
print("✓ Test 3: Genre validation using tuples")
print("✓ Test 4: Borrow limit enforcement (3 books max)")
print("✓ Test 5: Book deletion restriction (borrowed copies)")
print("✓ Test 6: Member deletion restriction (borrowed books)")
print("✓ Test 7: Return book functionality")
print("✓ Test 8: Search functionality")