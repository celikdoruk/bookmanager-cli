import sqlite3
from pathlib import Path

class Database:
    def __init__(self, db_name: str | Path = "database.db") -> None:
        self.db_name = db_name
        self._create_schema()

    def _connect(self) -> sqlite3.Connection:
        conn = sqlite3.connect(self.db_name)
        conn.row_factory = sqlite3.Row
        return conn

    def _create_schema(self) -> None:
        with self._connect() as conn:
            conn.execute("""
                            CREATE TABLE IF NOT EXISTS books (
                                id integer PRIMARY KEY AUTOINCREMENT,
                                name text,
                                page_num integer,
                                status text
                                    );
                        """)

    def exists(self, id: int) -> bool:
        with self._connect() as conn:
            cursor = conn.execute("SELECT 1 FROM books WHERE id = ?", (id,))
            return cursor.fetchone() is not None

    def insert(self, name: str, page_num: int, status: str) -> int | None:
        with self._connect() as conn:
            cursor = conn.execute("INSERT INTO books (name, page_num, status) VALUES (?, ?, ?)", (name, page_num, status))
            return cursor.lastrowid

    def delete(self, id: int) -> None:
        with self._connect() as conn:
            conn.execute("DELETE FROM books WHERE id = ?", (id,))

    def fetch_all(self) -> list:
        with self._connect() as conn:
            cursor = conn.execute("SELECT * FROM books")
            return cursor.fetchall()

    def fetch_all_id(self) -> list:
        with self._connect() as conn:
            cursor = conn.execute("SELECT id FROM books")
            return cursor.fetchall()