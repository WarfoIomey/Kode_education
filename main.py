from fastapi import FastAPI

from auth.routes import router as auth_router
from user.routes import router as users_router
from note.routes import router as notes_router


app = FastAPI()

app.include_router(auth_router, prefix="/auth", tags=["auth"])
app.include_router(users_router, prefix="/users", tags=["users"])
app.include_router(notes_router, prefix="/notes", tags=["notes"])


@app.get("/")
def read_root():
    return {"This is a test assignment from Code Education"}
