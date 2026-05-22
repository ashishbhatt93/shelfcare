from pydantic import BaseModel, field_validator, EmailStr
import re

class RegisterRequest(BaseModel):
    name: str
    phone_number: str
    invite_code: str
    password: str
    email: EmailStr

    @field_validator("phone_number")
    @classmethod
    def validate_phone(cls, v):
        if not re.match(r"^[6-9]\d{9}$", v):
            raise ValueError("Please enter a valid 10 digit number")
        return v

class LoginRequest(BaseModel):
    phone_number: str
    password: str
