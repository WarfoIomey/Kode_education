from typing import List

from fastapi import APIRouter, Depends, HTTPException
from note.schemas import Note, NoteCreate
from note.models import Note as NoteModel
from user.schemas import User
from user.models import User as UserModel
from sqlalchemy.orm import Session

from auth.crud import get_db, get_note_current_user, get_current_user
from auth.utils import check_spelling


router = APIRouter()


@router.get("/note", response_model=List[Note])
def read_notes_me(current_user: UserModel = Depends(get_current_user), db: Session = Depends(get_db)):
    db_notes = get_note_current_user(db, user_id=current_user.id)
    if not db_notes:
        raise HTTPException(status_code=400, detail="There is not a single note")
    return db_notes


@router.post("/create_note", response_model=Note)
def create_note(note: NoteCreate, current_user: UserModel = Depends(get_current_user), db: Session = Depends(get_db)):
    db_note = NoteModel(
        title=note.title,
        content=note.content,
        user_id=current_user.id
    )
    text_note = note.content
    correct_word = check_spelling(text=text_note)
    for error in correct_word:
        text_note = text_note.replace(error["word"], error["s"][0])
    db_note = NoteModel(
        title=note.title,
        content=text_note,
        user_id=current_user.id
    )
    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    return db_note
