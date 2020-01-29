from fastapi import FastAPI
from fastalchemy import SQLAlchemyMiddleware, db

app = FastAPI()
app.add_middleware(SQLAlchemyMiddleware)

from models import User
import schemas

@app.post('/users', response_model=schemas.User)
def create_user(user: schemas.UserCreate):
    user = User(id=user.id, email=user.email)
    db.add(user)
    return user

@app.get('/users')
def get_users():
    '''Return users.'''
    users = db.query(User).order_by(User.id).all()
    return users
