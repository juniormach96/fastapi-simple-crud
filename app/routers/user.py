from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from .. import models, schemas, utils
from ..database import get_db
from sqlalchemy.exc import IntegrityError


router = APIRouter(
    prefix="/users",
    tags=['Users']
)

# /users/
# /users


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):

    # hash the password - user.password
    hashed_password = utils.hash(user.password)
    user.password = hashed_password

    new_user = models.User(**user.dict())
    try:
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user
    except IntegrityError:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail=f"This email is already registered")