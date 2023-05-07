import os
from dotenv import load_dotenv

load_dotenv('./secrets.env')

sLogLevel = os.environ.get('LOG_LEVEL', 'INFO').upper()

class Config:
    def __init__(self):
        self.openai_key = os.environ.get('OPENAI_API_KEY', "NOT PROVIDED")

    def __str__(self):
        return f"AI config"