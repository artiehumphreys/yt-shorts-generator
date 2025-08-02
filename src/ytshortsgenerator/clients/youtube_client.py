from googleapiclient.discovery import build
from ytshortsgenerator.auth import get_saved_credentials


class YouTubeClient:
    def __init__(self) -> None:
        self.creds = get_saved_credentials()
        self.youtube = build(
            serviceName="youtube", version="v3", credentials=self.creds
        )
