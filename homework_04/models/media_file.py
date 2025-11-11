from abc import ABC, abstractmethod
from datetime import datetime
from typing import Dict, Any

class MediaFile(ABC):
    """Абстрактный базовый класс для всех медиа-файлов"""
    
    def __init__(self, name: str, size: int, owner: str, created_at: datetime = None):
        self.name = name
        self.size = size
        self.owner = owner
        self.created_at = created_at or datetime.now()
        self._metadata: Dict[str, Any] = {}
    
    @property
    def file_type(self) -> str:
        """Тип файла (определяется в дочерних классах)"""
        return self.__class__.__name__.lower()
    
    @abstractmethod
    def get_specific_metadata(self) -> Dict[str, Any]:
        """Абстрактный метод для получения специфичных метаданных"""
        pass
    
    def get_all_metadata(self) -> Dict[str, Any]:
        """Получить все метаданные файла"""
        base_metadata = {
            'name': self.name,
            'size': self.size,
            'owner': self.owner,
            'created_at': self.created_at,
            'file_type': self.file_type
        }
        base_metadata.update(self.get_specific_metadata())
        return base_metadata
    
    def update_metadata(self, **kwargs):
        """Обновление метаданных"""
        self._metadata.update(kwargs)
    
    @abstractmethod
    def process(self, operation: str, **kwargs):
        """Абстрактный метод для обработки файла"""
        pass
    
    def __str__(self):
        return f"{self.file_type.capitalize()}({self.name}, {self.size} bytes, owner: {self.owner})"