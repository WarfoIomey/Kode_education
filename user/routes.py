from fastapi import APIRouter, Depends
from auth.crud import get_current_user
from user.schemas import User
from user.models import User as UserModel


router = APIRouter()


@router.get("/me", response_model=User)
def read_users_me(current_user: UserModel = Depends(get_current_user)):
    return current_user

