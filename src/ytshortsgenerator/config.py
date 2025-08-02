from dataclasses import dataclass
import os
from dotenv import load_dotenv

load_dotenv()

@dataclass
class Settings:
    reddit_client_id: str = os.getenv("REDDIT_CLIENT_ID")
    reddit_client_secret: str = os.getenv("REDDIT_CLIENT_SECRET")
    reddit_user_agent: str = os.getenv("REDDIT_USER_AGENT", "ytshortsgenerator/0.1")
    elevenlabs_api_key: str = os.getenv("ELEVENLABS_API_KEY")

settings = Settings()
