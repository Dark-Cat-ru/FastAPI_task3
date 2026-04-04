from pydantic import BaseModel, SecretStr, Field, ConfigDict

class BaseUser(BaseModel):
    login: str

class User(BaseUser):
    model_config = ConfigDict(from_attributes=True)
    password: SecretStr = Field(min_length=8)

class CreateUser(BaseUser):
    password: str