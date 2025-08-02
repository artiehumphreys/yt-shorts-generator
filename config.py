from dataclasses import dataclass
import os
from dotenv import load_dotenv

load_dotenv()

@dataclass
class Config:
	reddit_client_id: str = os.getenv("REDDIT_CLIENT_ID")
	reddit_client_secret: str = os.getenv("REDDIT_CLIENT_SECRET")

config = Config()
