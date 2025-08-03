from dataclasses import dataclass
import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()


@dataclass
class Settings:
    base_dir: Path = Path(__file__).resolve().parents[2]
    download_dir: Path = base_dir / "downloads"
    video_download_dir: Path = download_dir / "videos"
    audio_output_dir: Path = download_dir / "audio"

    reddit_client_id: str | None = os.getenv("REDDIT_CLIENT_ID")
    reddit_client_secret: str | None = os.getenv("REDDIT_CLIENT_SECRET")
    reddit_user_agent: str = os.getenv("REDDIT_USER_AGENT", "ytshortsgenerator/0.1")

    elevenlabs_api_key: str | None = os.getenv("ELEVENLABS_API_KEY")

    youtube_client_id: str | None = os.getenv("YOUTUBE_OAUTH_CLIENT_ID")
    youtube_client_secret: str | None = os.getenv("YOUTUBE_OAUTH_CLIENT_SECRET")

    def __post_init__(self):
        self.download_dir.mkdir(parents=True, exist_ok=True)
        self.video_download_dir.mkdir(parents=True, exist_ok=True)
        self.audio_output_dir.mkdir(parents=True, exist_ok=True)


settings = Settings()
