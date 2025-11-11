from abc import ABC, abstractmethod
from typing import BinaryIO, Optional

class Storage(ABC):
    """Абстрактный класс для систем хранения"""
    
    @abstractmethod
    def save(self, file_data: BinaryIO, file_path: str) -> bool:
        """Сохранить файл в хранилище"""
        pass
    
    @abstractmethod
    def load(self, file_path: str) -> Optional[BinaryIO]:
        """Загрузить файл из хранилища"""
        pass
    
    @abstractmethod
    def delete(self, file_path: str) -> bool:
        """Удалить файл из хранилища"""
        pass
    
    @abstractmethod
    def exists(self, file_path: str) -> bool:
        """Проверить существование файла"""
        pass
    
    @abstractmethod
    def get_file_url(self, file_path: str) -> Optional[str]:
        """Получить URL для доступа к файлу"""
        pass