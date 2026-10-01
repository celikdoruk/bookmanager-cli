import argparse
import sys

from tracker import BookManager

def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="Book Managemenet Software",
        description="Manage your books with this simple CLI tool."
    )
    
    subparsers = parser.add_subparsers(dest="command", required=True)
    
    add = subparsers.add_parser("add", help="add books to the repository")
    add.add_argument("-n", "--name")
    add.add_argument("-p", "--page-num", type=int)
    add.add_argument("-s", "--status")

    remove = subparsers.add_parser("remove", help="remove books from the repository")
    remove.add_argument("-id", required=True)

    subparsers.add_parser("list", help="list all the books an their information")

    return parser


def main() -> None:
    parser = create_parser()
    manager = BookManager("database.db")

    if len(sys.argv) < 2:
        parser.print_help()
        return

    arguments = parser.parse_args()

    try:
        match arguments.command:
            case "add":
                book = manager.add_book(
                    name=arguments.name,
                    page_num=arguments.page_num,
                    status=arguments.status
                )
                print(f"Book {book.name} added to the repository")
            
            case "remove":
                manager.delete_book(arguments.id)
                print(f"Book with id: {arguments.id} has been deleted.")

            case "list":
                books = manager.list_all_books()

                if not books:
                    print("no books in repository")

                for book in books:
                    print(book)
    
    except Exception as e:
        print(f"An error has occured: {e}")

if __name__ == "__main__":
    main()