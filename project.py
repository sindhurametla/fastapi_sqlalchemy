from fastapi import FastAPI, Depends
from database import get_db, engine
from sqlalchemy.orm import Session
from model import Book
from pydantic import BaseModel
from classes import BookStore

app = FastAPI()

@app.post('/books')
def create_book(book: BookStore, db:Session = Depends(get_db)):
    new_book = Book(id = book.id, title = book.title,author = book.author, publish_date = book.publish_date, copies_sold = book.copies_sold)               
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book

@app.get('/books')
def get_books(db: Session = Depends(get_db)):
    books = db.query(Book).all()
    return books

@app.put('/books/{book_id}')
def update_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(Book).filter(Book.id == book_id).first()

    if book:
        book.copies_sold = "40000"
        db.commit()
        db.refresh(book)
        return book

    return {"message": "Book not found"}

@app.delete('/books/{book_id}')
def delete_book(book_id: int, db: Session = Depends(get_db)):

    book = db.query(Book).filter(Book.id == book_id).first()

    if book:
        db.delete(book)
        db.commit()

        return {"message": "Book deleted successfully"}

    return {"message": "Book not found"}
