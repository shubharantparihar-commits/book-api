from fastapi import FastAPI, HTTPException

app = FastAPI()

books = [
    {"book_id": 1, "title": "Dune", "author": "Frank Herbert", "year": 1965, "genre": "Sci-Fi", "price": 18.99},
    {"book_id": 2, "title": "Dune Messiah", "author": "Frank Herbert", "year": 1969, "genre": "Sci-Fi", "price": 16.50},
    {"book_id": 3, "title": "The Hobbit", "author": "J.R.R. Tolkien", "year": 1937, "genre": "Fantasy", "price": 14.99},
    {"book_id": 4, "title": "The Fellowship of the Ring", "author": "J.R.R. Tolkien", "year": 1954, "genre": "Fantasy", "price": 19.99},
    {"book_id": 5, "title": "1984", "author": "George Orwell", "year": 1949, "genre": "Dystopian", "price": 12.99},
    {"book_id": 6, "title": "Animal Farm", "author": "George Orwell", "year": 1945, "genre": "Dystopian", "price": 10.50},
    {"book_id": 7, "title": "Foundation", "author": "Isaac Asimov", "year": 1951, "genre": "Sci-Fi", "price": 15.75},
    {"book_id": 8, "title": "I, Robot", "author": "Isaac Asimov", "year": 1950, "genre": "Sci-Fi", "price": 13.99},
    {"book_id": 9, "title": "Murder on the Orient Express", "author": "Agatha Christie", "year": 1934, "genre": "Mystery", "price": 11.99},
    {"book_id": 10, "title": "And Then There Were None", "author": "Agatha Christie", "year": 1939, "genre": "Mystery", "price": 12.50},
    {"book_id": 11, "title": "Pride and Prejudice", "author": "Jane Austen", "year": 1813, "genre": "Romance", "price": 9.99},
    {"book_id": 12, "title": "Sense and Sensibility", "author": "Jane Austen", "year": 1811, "genre": "Romance", "price": 10.99},
    {"book_id": 13, "title": "Atomic Habits", "author": "James Clear", "year": 2018, "genre": "Self-Help", "price": 21.00},
    {"book_id": 14, "title": "Sapiens", "author": "Yuval Noah Harari", "year": 2011, "genre": "History", "price": 22.50},
    {"book_id": 15, "title": "Homo Deus", "author": "Yuval Noah Harari", "year": 2015, "genre": "History", "price": 23.00},
]

@app.get("/books")
def get_books(skip: int = 0, limit: int = 10, q: str | None = None):
    results = books
    if q is not None:
        results = [book for book in books if q.lower() in book["title"].lower()]
    return results[skip: skip + limit]


@app.get("/books/stats")
def get_book_stats():
    total_books = len(books)
    if total_books == 0:
        return {
            "total_books": 0,
            "average_price": 0.0,
            "genres": {}
        }
    total_price = sum(book["price"] for book in books)
    average_price = round(total_price/ total_books, 2)
    
    genre_counts = {}
    for book in books:
        genre = book["genre"]
        genre_counts[genre] = genre_counts.get(genre, 0) + 1
    return {
        "total_books": total_books,
        "average_price": average_price,
        "genres": genre_counts
    }


@app.get("/books/{book_id}")
def get_book_by_id(book_id: int):
    book = next((book for book in books if book["book_id"] == book_id),None)
    if book is None:
        raise HTTPException(status_code = 404, detail ="Book not found")
    return book
    

