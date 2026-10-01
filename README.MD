# Book Tracker

A simple command-line tool for keeping track of the books you're reading. Add books with their page count and reading status, list them, and remove them. Everything is stored locally in a SQLite database.

## Features

- Add a book with its name, number of pages, and status
- List all the books in your collection
- Remove a book by its id
- Local storage with SQLite, no external dependencies

## Requirements

- Python 3.10 or newer (the code uses `match` statements and `X | None` type hints)

No third-party packages are needed. `sqlite3` and `argparse` are part of the standard library.

## Usage

Run the tool from the project folder. The database file (`database.db`) is created automatically on first run.

**Add a book**

```bash
python main.py add -n "Dune" -p 612 -s "not started"
```

Options:

| Flag | Description |
| --- | --- |
| `-n`, `--name` | Title of the book |
| `-p`, `--page-num` | Number of pages |
| `-s`, `--status` | One of `in progress`, `finished`, `not started` |

**List all books**

```bash
python main.py list
```

**Remove a book**

```bash
python main.py remove -id 1
```

Use `python main.py --help` or `python main.py <command> --help` to see all options.

## Project structure

```
book-tracker/
├── main.py          # CLI entry point (argparse)
├── tracker.py       # BookManager: the logic between the CLI and the database
├── repository.py    # Database class: all SQLite queries
├── model.py         # Book dataclass
└── exception.py     # BookException
```

The project is split into layers: `main.py` handles user input, `tracker.py` holds the application logic, and `repository.py` is the only file that talks to the database.

## Possible improvements

- Update a book's status (for example, from "in progress" to "finished")
- Filter the list by status
- Track pages read, not just total pages
- Add automated tests