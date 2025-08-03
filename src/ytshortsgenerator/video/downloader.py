from pathlib import Path
from ytshortsgenerator.config import settings


class VideoDownloaderClient:
    def __init__(self):
        self.download_dir = settings.video_download_dir
