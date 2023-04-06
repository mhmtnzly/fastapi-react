from pydantic import BaseModel, Field, EmailStr
import uuid
import datetime


class User(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    firstname: str = Field(min_length=2, max_length=30)
    lastname: str = Field(min_length=2, max_length=30)
    username: str = Field(min_length=8, max_length=20)
    email: EmailStr = Field(...)
    password: str = Field(...)
    public_id: str = uuid.uuid4()
    create_date: str = datetime.datetime.now()

    class Config:
        schema_extra = {
            "example": {
                "firstname": "Firstname",
                "lastname": "Lastname",
                "username": "username",
                "email": "email@email.com",
                "password": "password"
            }
        }


class RegisterReturn(BaseModel):
    firstname: str = Field(min_length=2, max_length=30)
    lastname: str = Field(min_length=2, max_length=30)
    username: str = Field(min_length=8, max_length=20)
    email: EmailStr = Field(...)
