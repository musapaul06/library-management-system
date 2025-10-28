# 📚 Mini Library Management System

### Author: Paul Kizz  
*Course:* PROG211 – Object-Oriented Programming 1  
*Language:* Python  
*Version:* 1.0  
## 🧾 Overview

The *Mini Library Management System* is a simple Python-based console application designed to manage basic library operations. It helps librarians or users to *add books, **register members, **borrow and return books, and **search for books* easily.  

The system makes use of *Python dictionaries, lists, and tuples* to store and manage library data efficiently. It’s lightweight, user-friendly, and ideal for beginners learning data structures and object-oriented programming concepts.

## 🧠 Features

✅ *Add Book* – Register new books with ISBN, title, author, genre, and copies.  
✅ *Add Member* – Add new library members with unique IDs and email addresses.  
✅ *Search Books* – Find books by title or author keyword.  
✅ *Update Book* – Edit book details like title, author, genre, or copies.  
✅ *Delete Book* – Remove a book record from the system.  
✅ *Borrow Book* – Allow members to borrow books (up to 3 at a time).  
✅ *Return Book* – Handle book returns from members.  
✅ *View All Books* – Display all available books in the system.  
✅ *Menu System* – Interactive command-line interface for easy navigation.

## 🏗 Data Structures Used

| Data Structure | Variable Name | Purpose |
|----------------|----------------|----------|
| **Dictionary (dict)** | books | Stores all book details such as title, author, genre, and total copies using the ISBN as the key. |
| **List (list)** | members | Keeps track of all library members and their borrowed books. |
| **Tuple (tuple)** | genres | Contains a fixed list of valid book genres (e.g., Fiction, Non-Fiction, Science, etc.). |

These structures make the system simple, efficient, and easy to extend.

## ⚙ How to Run the Program

### 🖥 Requirements
- Python 3.8 or above  
- A terminal or IDE (like *VS Code* or *PyCharm*)

### ▶ Steps
1. *Download or copy* the project file:  
   mini_library_system.py
2. Open the file in your IDE or terminal.
3. Run the command below:
   ```bash
   python mini_library_system.py
