from fastapi import FastAPI, Path
from pydantic import BaseModel
from typing import Annotated
#uvicorn module_16_1:app --reload
class Item(BaseModel):
    name: str
    price: float

users = {'1': 'Имя: Example, возраст: 18'}
app = FastAPI()

@app.get("/")
async def Get_Main_Page()-> dict:
    return {"message": "Главная страница"}

@app.get("/user/admin")
async def get_admin_page()-> dict:
    return {"message": "Вы вошли как администратор"}

@app.get("/user/{user_id}")
async def get_user_number(user_id: int) :
    return {f"Вы вошли как пользователь № {user_id}"}

@app.get("/user")
async def get_user_info(username,age) -> dict:
    return {"message":f"Информация о пользователе. Имя: {username}, Возраст: {age}"}


