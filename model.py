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


class User(BaseModel):
    username: str = Field(
        ...,
        min_length=3,
        max_length=50
    )