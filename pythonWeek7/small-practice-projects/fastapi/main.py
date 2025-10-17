from fastapi import FastAPI 
from pydantic import BaseModel
from typing import Optional, List

app = FastAPI()

class UserModel(BaseModel):
    name: str
    age: int
    company: str

user_list: List[UserModel] = [] 

@app.get("/")
async def root():
    return { 'Hello': "World" }

@app.post("/users")
def post_user(user: UserModel):
    user_list.append(user)
    return { "message": "User Created", "user": user}

@app.get("/users")
async def get_users() -> List[UserModel]:
    return user_list