from dataclasses import dataclass
from typing import Literal


@dataclass
class Book:
    id: int | None
    name: str
    page_num: int
    status: Literal["in progress", "finished", "not started"]


    def __repr__(self) -> str:
        return f"book name: {self.name}, with {self.page_num} pages"

