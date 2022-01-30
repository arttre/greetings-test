from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from ..database import database_init
from ..models.users import User
from ..utils.users import greeting, view_all

router = APIRouter(
    tags=['Greeting with users'],
    prefix="/users"
)

get_db = database_init.get_db


@router.post('/greeting')
def greeting_with_user(user_for_greeting: User, database: Session = Depends(get_db)):
    return greeting(user_for_greeting, database)


@router.get('/view_all')
def view_all_users(database: Session = Depends(get_db)):
    return view_all(database)
