from pydantic import BaseModel


class NewPost(BaseModel):
    title: str
    content: str