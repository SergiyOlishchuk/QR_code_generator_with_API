import os

from dotenv import load_dotenv

load_dotenv()


class Settings:
    def __init__(self):
        try:
            self.APP_PORT = int(os.getenv("API_PORT", 8080))
        except ValueError:
            print("APP_PORT have to be INTEGER!")
            exit(1)

        if self.APP_PORT > 9999:
            print("APP_PORT have to be LESS THAN 9999")
            exit(1)


settings = Settings()
