import os
from pathlib import Path
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()


@dataclass
class Settings:
    base_dir: Path = Path(__file__).resolve().parents[2]
    result_dir: Path = base_dir / "output"
    download_dir: Path = base_dir / "downloads"
    video_download_dir: Path = download_dir / "videos"
    audio_output_dir: Path = download_dir / "audio"
    font: str = "BubblegumSans-Regular.ttf"
    font_path: Path = base_dir / "fonts" / font

    def __post_init__(self):
        for d in (
            self.download_dir,
            self.video_download_dir,
            self.audio_output_dir,
            self.result_dir,
        ):
            d.mkdir(parents=True, exist_ok=True)

    @property
    def reddit_client_id(self) -> str | None:
        return os.getenv("REDDIT_CLIENT_ID")

    @property
    def reddit_client_secret(self) -> str | None:
        return os.getenv("REDDIT_CLIENT_SECRET")

    @property
    def reddit_user_agent(self) -> str:
        return os.getenv("REDDIT_USER_AGENT", "ytshortsgenerator/0.1")

    @property
    def elevenlabs_api_key(self) -> str | None:
        return os.getenv("ELEVENLABS_API_KEY")

    @property
    def youtube_client_id(self) -> str | None:
        return os.getenv("YOUTUBE_OAUTH_CLIENT_ID")

    @property
    def youtube_client_secret(self) -> str | None:
        return os.getenv("YOUTUBE_OAUTH_CLIENT_SECRET")


_settings: Settings | None = None


def get_settings() -> Settings:
    global _settings
    if _settings is None:
        _settings = Settings()
    return _settings


settings = get_settings()
