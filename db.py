from motor.motor_asyncio import AsyncIOMotorClient
from config import settings

class Database:
    def __init__(self, db_url: str, db_name: str):
        self.client = AsyncIOMotorClient(db_url)
        self.db = self.client[db_name]

db = Database(settings.DB_URL, settings.DB_NAME)
