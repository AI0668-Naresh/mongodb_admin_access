from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from crud import create_admin_user, get_admin_user, list_all_users
from models import AdminUser, AdminUserInDB

router = APIRouter()

class AdminUserRequest(BaseModel):
    username: str
    password: str
    role: str = "admin"

@router.post("/admin/")
async def create_admin(admin_user: AdminUserRequest):
    user_in_db = await create_admin_user(admin_user)
    return user_in_db

@router.get("/admin/{username}")
async def get_admin(username: str):
    user = await get_admin_user(username)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.get("/admins/")
async def get_all_admins():
    users = await list_all_users()
    return users
