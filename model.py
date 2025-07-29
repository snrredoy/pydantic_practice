from pydantic import BaseModel, Field, field_validator, model_validator, computed_field
from typing import Optional, List, Dict, Set

class Cart(BaseModel):
    user_id : int
    items: List[str]
    quantity: Dict[str, int]

class BlogPost(BaseModel):
    title: str
    description: str
    image_url: Optional[str] = None


class Employee(BaseModel):
    id: int
    name:str = Field(
        ...,
        min_length=3,
        max_length=50,
        description='Employee name',
        example='John Doe'
    )
    department: Optional[str] = 'Engineering'
    salary: float = Field(
        ...,
        ge=10000,
    )
    


class User(BaseModel):
    username: str

    @field_validator('username')
    def username_length(cls, value):
        if len(value) < 3:
            raise ValueError('Username must be at least 3 characters long')
        return value


class SignUpData(BaseModel):
    username: str
    password: str
    confirm_password: str

    @model_validator(mode='after')
    def password_match(cls, values):
        if values.password != values.confirm_password:
            raise ValueError('Password not match')
        return values


class Product(BaseModel):
    price: float
    quantity: int

    @computed_field
    @property
    def total_price(self) -> float:
        return self.price * self.quantity


class Address(BaseModel):
    street: str
    city: str
    state: str
    zip_code: str


class UserProfile(BaseModel):
    id : int
    full_name: str
    address: Address


class Comment(BaseModel):
    id: int
    content: str
    author: UserProfile
    replies: Optional[List['Comment']] = None

Comment.model_rebuild()  # To handle recursive type definition forward referencing