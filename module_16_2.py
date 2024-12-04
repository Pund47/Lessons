from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

#@app.get("/user/{username}/{age}")
#async def get_user(username : Annotated[str, Path(min_length=5,max_length=20,description="Enter username",example="UrbanUser")],
#                         age: Annotated[int, Path(ge=18,le=120,description="Enter age",example="24")]) -> dict:
#    return {"message":f"Информация о пользователе. Имя: {username}, Возраст: {age}"}

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
async def get_user_number(user_id:Annotated[int, Path(ge=0,le=100,description="Enter ID")]) :
    return {f"Вы вошли как пользователь № {user_id}"}

@app.get("/user")
async def get_user_info(username: Annotated[str, Path(min_length=5,max_length=20,description="Enter username",example="UrbanUser")],
                             age: Annotated[int, Path(ge=18,le=120,description="Enter age",example="24")]) -> dict:
    return {"message":f"Информация о пользователе. Имя: {username}, Возраст: {age}"}
