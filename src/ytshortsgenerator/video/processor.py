from ytshortsgenerator.config import settings
from pathlib import Path


class VideoProcessor:
    def __init__(
        self,
        ffmpeg_path: str = "ffmpeg",
        default_codec: str = "libx264",
        audio_codec: str = "aac",
        pixel_fmt: str = "yuv420p",
        shortest: bool = True,
    ) -> None:
        self.ffmpeg_path = ffmpeg_path
        self.default_codec = default_codec
        self.audio_codec = audio_codec
        self.pixel_fmt = pixel_fmt
        self.shortest = shortest
