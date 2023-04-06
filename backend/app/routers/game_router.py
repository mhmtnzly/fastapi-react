
from fastapi import (APIRouter, status, Request, Body,
                     HTTPException)
from fastapi.encoders import jsonable_encoder
from ..models.model import User, RegisterReturn
from ..auth.auth import get_password_hash
from ..crud.crud import find_email, find_username

router = APIRouter()


@router.post("/register", response_description="SignUp",
             status_code=status.HTTP_201_CREATED,
             response_model=RegisterReturn)
async def register(request: Request, user: User = Body(...)):
    user = jsonable_encoder(user)
    if find_email(user["email"], request.app.database["users"]):
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="You have already had an account with the email.",
            headers={"WWW-Authenticate": "Bearer"})
    elif find_username(user["username"], request.app.database["users"]):
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Choose a different username.",
            headers={"WWW-Authenticate": "Bearer"})
    hashed_password = get_password_hash(user["password"])
    user["password"] = hashed_password
    new_user = request.app.database["users"].insert_one(user)
    created_user = request.app.database["users"].find_one(
        {"_id": new_user.inserted_id})
    return created_user
