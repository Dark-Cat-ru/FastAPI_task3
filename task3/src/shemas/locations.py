from pydantic import BaseModel, Field

class Location(BaseModel):
    name: str = Field(max_length=20, min_length=3)