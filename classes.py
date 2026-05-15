from pydantic import BaseModel

class BookStore(BaseModel):
    id: int
    title: str
    author: str
    publish_date: str
    copies_sold: str