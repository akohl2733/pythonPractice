from fastapi import FastAPI, Depends
from pydantic import BaseModel
from typing import Optional, List
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase, Mapped, mapped_column
import sys, os


app = FastAPI()


# SQLite DB setup
class Base(DeclarativeBase):
    pass

DATABASE_URL = ("sqlite:///./test.db")
engine = create_engine(DATABASE_URL, echo=True)

class User(Base):
    __tablename__ = "user_info"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    age: Mapped[int]
    company: Mapped[str]

Base.metadata.create_all(bind=engine)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)


class UserModel(BaseModel):
    name: str
    age: int
    company: str

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def root():
    return { 'Hello': "World" }


@app.post("/users")
def post_user(user: UserModel, db: SessionLocal = Depends(get_db)):
    user_data = user.model_dump()
    db_user = User(**user_data)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return { "message": "User Created", "user": user}


@app.get("/users")
async def get_users(db: SessionLocal = Depends(get_db)) -> List[UserModel]:
    users = db.query(User).all()
    return users