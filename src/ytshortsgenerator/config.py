from dataclasses import dataclass
import os
from dotenv import load_dotenv

load_dotenv()


@dataclass
class Settings:
    reddit_client_id: str | None = os.getenv("REDDIT_CLIENT_ID")
    reddit_client_secret: str | None = os.getenv("REDDIT_CLIENT_SECRET")
    reddit_user_agent: str = os.getenv("REDDIT_USER_AGENT", "ytshortsgenerator/0.1")
    elevenlabs_api_key: str | None = os.getenv("ELEVENLABS_API_KEY")
    youtube_client_id: str | None = os.getenv("YOUTUBE_OAUTH_CLIENT_ID")
    youtube_client_secret: str | None = os.getenv("YOUTUBE_OAUTH_CLIENT_SECRET")


settings = Settings()
