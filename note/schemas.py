from pydantic import BaseModel


class NoteBase(BaseModel):
    id: int
    title: str
    content: str


class NoteCreate(BaseModel):
    title: str
    content: str

    class Config:
        orm_mode = True


class Note(NoteBase):
    id: int
    content: str

    class Config:
        orm_mode = True
