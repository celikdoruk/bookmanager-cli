from model import Book
from repository import Database
from exception import BookException

class BookManager:
    STATUS = ["in progress", "finished", "not started"]

    def __init__(self, db_name) -> None:
        self.db = Database(db_name)

    def add_book(self, name: str, page_num: int, status: str) -> Book:
        if not all([name, page_num, status]):
            raise ValueError("Please provide all arguments.")

        books = self.db.fetch_all()
        names = [book["name"] for book in books]
        if name in names:
            raise BookException("Book already in database.")

        if status.lower() not in self.STATUS:
            raise BookException("Please provide a valid status")

        if not 1 <= page_num <= 5000:
            raise BookException("A book must have pages between 1 and 5000.")

        if not name:
            raise BookException("Please provide a book name")

        book_id = self.db.insert(name, page_num, status)

        return Book(
            id = book_id,
            name=name,
            page_num=page_num,
            status=status # type: ignore
        )

    def delete_book(self, id: int) -> None:
        book = self.db.exists(id)

        if not book:
            raise BookException("book not in repository")

        self.db.delete(id)

    def list_all_books(self) -> list[Book]:
        books = self.db.fetch_all()
        return [
            Book(id=book["id"], name=book["name"], page_num=book["page_num"], status=book["status"])
            for book in books]
