from fastapi import APIRouter

router = APIRouter(prefix="/task", tags=["task"])

@router.get("/")
async def get_all_tasks():
    pass

@router.get("/task_id")
async def tasks_by_id():
    pass



@router.post("/create")
async def create_task():
    pass

@router.put("/update_category")
async def update_task():
    pass

@router.delete("/delete")
async def delete_task():
    pass