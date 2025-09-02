"""
Library Management System

Task:
- Create functions to manage a library using dictionaries and lists.
- Each book is stored in a dictionary with fields: { "id": int, "title": str, "author": str, "available": bool }
- Users can borrow and return books.
- Support *args for searching books by multiple fields (title, author).
- Support **kwargs for adding optional book details like "year", "genre".


// NOT FOR THIS ASSIGNMENT
Future OOP Extension:
- Books as a Book class.
- Library as a Library class with borrow() and return() methods.
"""

library = []

def add_book(book_id,title,author,**kwargs):
    """Add a new book into the library with flexible details.
        return "Book {book_title} added successfully!"
    """
    book = {
        "id":id,
        "title":title,
        "author":author,
        "available":True
    }
    book.update(kwargs)
    library.append(book)
    return f"sucessfully added {title} into the dictionary"



def search_books(search_param):
    """Search for books by multiple keywords (title, author).
    reaturn books that match search description.
    """
    if not search_param:
        return library

    book_results = []
    for book in library:
        title_match = any(term in book["title"].lower() for term in search_terms)
        author_match = any(term in book["title"].lower() for term in search_terms)
        if title_match or author_match:
            book_results.append(book)
    return book_results

def borrow_book(book_id):
    """Borrow a book if available (msg: You borrowed {book_title}).
        else-> msg: Book {book_title} not available
    """
    for book in library:
        if book["id"] == book_id:
            if book["available"] :
                book["available"] = False
                return  f"successfully borrowed {book['title']}"
            else: 
                return f"{book['title']} not  available"
    return "Such book does not exist"
print(borrow_book(1))
