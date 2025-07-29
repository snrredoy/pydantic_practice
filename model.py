from pydantic import BaseModel, Field
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
    username: str = Field(
        ...,
        min_length=3,
        max_length=50
    )