from .media_file import MediaFile
from typing import Dict, Any

class VideoFile(MediaFile):
    """Класс для видео файлов"""
    
    def __init__(self, name: str, size: int, owner: str,
                 duration: float, resolution: str, fps: float):
        super().__init__(name, size, owner)
        self.duration = duration
        self.resolution = resolution
        self.fps = fps
    
    def get_specific_metadata(self) -> Dict[str, Any]:
        return {
            'duration': self.duration,
            'resolution': self.resolution,
            'fps': self.fps,
            'codec': getattr(self, 'codec', 'h264')  # Пример дополнительного поля
        }
    
    def process(self, operation: str, **kwargs):
        if operation == 'convert':
            print(f"Converting video file {self.name} to {kwargs.get('format', 'mp4')}")
        elif operation == 'extract_frame':
            # Извлечение кадра в определенный момент времени
            timestamp = kwargs.get('timestamp', 0)
            print(f"Extracting frame at {timestamp}s from {self.name}")
        elif operation == 'compress':
            print(f"Compressing video file {self.name}")
        else:
            print(f"Unknown operation '{operation}' for video file")