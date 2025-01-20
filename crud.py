from db import db
from models import AdminUser, AdminUserInDB
from bson import ObjectId
from typing import List

# Function to create a new admin user
async def create_admin_user(admin_user: AdminUser) -> AdminUserInDB:
    user_dict = admin_user.dict()
    result = await db.db["users"].insert_one(user_dict)
    user_dict["id"] = str(result.inserted_id)
    return AdminUserInDB(**user_dict)

# Function to get a user by username
async def get_admin_user(username: str) -> AdminUserInDB:
    user = await db.db["users"].find_one({"username": username})
    if user:
        user["id"] = str(user["_id"])
        return AdminUserInDB(**user)
    return None

# Function to list all users (for admin use)
async def list_all_users() -> List[AdminUserInDB]:
    users = await db.db["users"].find().to_list(length=100)
    return [AdminUserInDB(**user) for user in users]
