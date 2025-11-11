import os
from pathlib import Path
from typing import BinaryIO, Optional
from .base import Storage

class LocalStorage(Storage):
    """Локальное файловое хранилище"""
    
    def __init__(self, base_path: str):
        self.base_path = Path(base_path)
        self.base_path.mkdir(parents=True, exist_ok=True)
    
    def save(self, file_data: BinaryIO, file_path: str) -> bool:
        try:
            full_path = self.base_path / file_path
            full_path.parent.mkdir(parents=True, exist_ok=True)
            
            with open(full_path, 'wb') as f:
                f.write(file_data.read())
            return True
        except Exception as e:
            print(f"Error saving file: {e}")
            return False
    
    def load(self, file_path: str) -> Optional[BinaryIO]:
        try:
            full_path = self.base_path / file_path
            return open(full_path, 'rb')
        except Exception as e:
            print(f"Error loading file: {e}")
            return None
    
    def delete(self, file_path: str) -> bool:
        try:
            full_path = self.base_path / file_path
            if full_path.exists():
                full_path.unlink()
                return True
            return False
        except Exception as e:
            print(f"Error deleting file: {e}")
            return False
    
    def exists(self, file_path: str) -> bool:
        full_path = self.base_path / file_path
        return full_path.exists()
    
    def get_file_url(self, file_path: str) -> Optional[str]:
        return f"file://{self.base_path / file_path}"