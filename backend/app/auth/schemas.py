from pydantic import BaseModel, field_validator
import re


class RegisterRequest(BaseModel):
    phone: str
    invite_code: str


    @field_validator("phone")
    def validate_phone(cls, v):
        if not re.fullmatch(r"\d{10}", v):
            raise ValueError("Phone number must be exactly 10 digits")
        return v
