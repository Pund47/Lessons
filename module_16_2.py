from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

@app.get("/user/{username}/{age}")
async def get_user(username : Annotated[str, Path(min_length=5,max_length=20,description="Enter username",example="UrbanUser")],
                         age: Annotated[int, Path(ge=18,le=120,description="Enter age",example="24")]) -> dict:
    return {"message":f"Информация о пользователе. Имя: {username}, Возраст: {age}"}