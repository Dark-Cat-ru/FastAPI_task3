from pydantic import BaseModel, SecretStr, Field

class BaseUser(BaseModel):
    login: str

class User(BaseUser):
    password: SecretStr = Field(min_length=8)

class CreateUser(BaseUser):
    password: str