import os

class Settings:
    DB_URL: str = os.getenv("MONGO_DB_URL", "mongodb://localhost:27017")
    DB_NAME: str = os.getenv("MONGO_DB_NAME", "adminDB")

    DB_URL = DB_URL.replace("\"", "")

    def load_url(self):
        with open("urls.txt","r") as f:
            self.DB_URL = f.read().strip()

settings = Settings()
