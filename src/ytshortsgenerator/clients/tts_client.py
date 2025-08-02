import os
from elevenlabs.client import ElevenLabs
from ytshortsgenerator.config import settings


class TTSClient:
    def __init__(self) -> None:
        api_key = settings.elevenlabs_api_key
        self.eleven = ElevenLabs(api_key=api_key)
