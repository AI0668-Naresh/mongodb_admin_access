from pydantic import BaseModel, Field
from typing import Optional

class AdminUser(BaseModel):
    username: str
    password: str
    role: Optional[str] = "admin"

class AdminUserInDB(AdminUser):
    id: str
