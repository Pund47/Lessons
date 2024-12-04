from fastapi import FastAPI, status, Body, HTTPException
from pydantic import BaseModel
from typing import List
#uvicorn module_16_4:app --reload

app = FastAPI()

users = []

class User(BaseModel):
     id: int #- номер пользователя(
     username: str #- имя пользователя(
     age: int #)- возраст пользователя(

@app.get("/users")
async def root1()-> List[User]:
    return users

@app.post('/user/{username}/{age}')
async def add_new_user(user:User, username,age) -> str:
   current_index = 0
   if len(users)== 0:
       current_index = 1
   else:
       current_index = (len(users) + 1)
   User.id = current_index
   User.username = username
   User.age = age
   users.append(User)
   return (f"User {current_index} is registered")

#put запрос по маршруту '/user/{user_id}/{username}/{age}'
@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user:User,user_id:int,username:str,age:int)-> str:
    try:
        edit_user = users[user_id]
        edit_user.username = username
        edit_user.age = age
        return (f"User updated!")
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")


@app.delete('/user/{user_id}')
async def del_user(user_id:int)-> str:
    try:
        users.pop(user_id)
        return (f"Пользователь {user_id} был удалён!")
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")
