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
async def add_new_user(user:User, username:str,age:int) -> str:
   if len(users)== 0:
       current_index = 1
   else:
       max_id = 0
       for i in range(1,len(users)):
           if int(users[i].id) > max_id:
               max_id = int(users[i].id)
       current_index = int(max_id + 1)
   User.id = current_index
   User.username = username
   User.age = age
   #users[current_index] = (username, age)
   users.append(User)
   return (f"User {User} is registered")

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
        userForDel = users[user_id]
        users.pop(user_id)
        return (f"Пользователь {userForDel} был удалён!")
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")
