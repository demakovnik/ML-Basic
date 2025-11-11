from .media_file import MediaFile
from typing import Dict, Any

class AudioFile(MediaFile):
    """Класс для аудио файлов"""
    
    def __init__(self, name: str, size: int, owner: str, 
                 duration: float, bitrate: int, sample_rate: int):
        super().__init__(name, size, owner)
        self.duration = duration
        self.bitrate = bitrate
        self.sample_rate = sample_rate
    
    def get_specific_metadata(self) -> Dict[str, Any]:
        return {
            'duration': self.duration,
            'bitrate': self.bitrate,
            'sample_rate': self.sample_rate,
            'channels': getattr(self, 'channels', 2)  # Пример дополнительного поля
        }
    
    def process(self, operation: str, **kwargs):
        if operation == 'convert':
            # Логика конвертации аудио
            print(f"Converting audio file {self.name} to {kwargs.get('format', 'mp3')}")
        elif operation == 'extract_features':
            # Извлечение аудио-фич (тональность, темп и т.д.)
            print(f"Extracting features from {self.name}")
        else:
            print(f"Unknown operation '{operation}' for audio file")