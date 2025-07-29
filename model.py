from pydantic import BaseModel, Field, field_validator, model_validator, computed_field, ConfigDict
from typing import Optional, List, Dict, Set
from datetime import datetime

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
    created_at: datetime

    model_config = ConfigDict(
        json_encoders = {
            datetime: lambda v: v.strftime('%d-%m-%Y %H:%M:%S')
        }
    )


class Comment(BaseModel):
    id: int
    content: str
    author: UserProfile
    replies: Optional[List['Comment']] = None

Comment.model_rebuild()  # To handle recursive type definition forward referencing


user = UserProfile(
    id=1,
    full_name="John Smith",
    created_at=datetime(2023, 10, 1, 12, 0, 0),
    address=Address(
        street="123 Main St",
        city="Anytown",
        state="CA",
        zip_code="12345"
    )
)

# using model_dump
user_dict = user.model_dump()
print(user_dict)

# using model_dump_json
user_json = user.model_dump_json()
print(user_json)