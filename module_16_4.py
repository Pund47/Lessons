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
       max_id = 1
       for i in range(1,len(users)):
           if int(users[i].id) > max_id:
               max_id = int(users[i].id)
       current_index = int(max_id + 1)
   user.id = current_index
   user.username = username
   user.age = age
   users.append(user)
   return (f"User {user} is registered")

#put запрос по маршруту '/user/{user_id}/{username}/{age}'
@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user:User,user_id:int,username:str,age:int)-> str:
    try:
        user = users[user_id]
        user.username = username
        user.age = age
        return (f"User {user} updated!")
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")


@app.delete('/user/{user_id}')
async def del_user(user:User,user_id:int)-> str:
    try:
        for i in range(0,len(users)):
            if users[i].id ==user_id:
                user_for_del = users[i]
                index_for_dell = i

        #user = user_for_del
        users.pop(index_for_dell)
        return (f"Пользователь {user_for_del} был удалён!")
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")
