from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    price: float


app = FastAPI()

@app.get("/")
async def root1()-> dict:
    return {"message": "Главная страница"}

@app.get("/user/{username}/{age}")
async def get_user(username : str, age: int) -> dict:
    return {"message":f"Информация о пользователе. Имя: {username}, Возраст: {age}"}


@app.get("/user/{user_id}")
async def get_user(user_id: int) :
    return {f"Вы вошли как пользователь № {user_id}"}

@app.get("/user/admin")
async def root11()-> dict:
    return {"message": "Вы вошли как администратор"}



