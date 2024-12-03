from fastapi import FastAPI
from typing import Annotated

app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}

@app.get("/users")
async def root1()-> dict:
    return users

@app.post('/user/{username}/{age}')
async def add_user(username,age) -> str:
    current_index = str(int(max(users,key=int))+1)
    users[current_index] = (username,age)
    return (f"User {current_index} is registered")

@app.put('/user/{user_id}/{username}/{age}')
async def update_users(user_id,username,age) -> str:
    users[user_id] = (username,age)
    return (f"The user {user_id} is updated")

@app.delete('/user/{user_id}')
async def del_user(user_id)-> str:
    users.pop(user_id)
    return (f"Пользователь {user_id} был удалён!")





