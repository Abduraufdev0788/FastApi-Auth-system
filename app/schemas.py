from pydantic  import BaseModel, Field, EmailStr

class UserCreate(BaseModel):
    first_name:str    = Field(min_length=3, max_length=64)
    last_name:str     = Field(min_length=3, max_length=64)
    email :str        = EmailStr()
    password:str      = Field(min_length=8)

