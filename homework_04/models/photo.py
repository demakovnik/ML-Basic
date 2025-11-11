from .media_file import MediaFile
from typing import Dict, Any

class PhotoFile(MediaFile):
    """Класс для фото файлов"""
    
    def __init__(self, name: str, size: int, owner: str,
                 resolution: str, camera_model: str = None):
        super().__init__(name, size, owner)
        self.resolution = resolution
        self.camera_model = camera_model
    
    def get_specific_metadata(self) -> Dict[str, Any]:
        return {
            'resolution': self.resolution,
            'camera_model': self.camera_model,
            'exif_data': getattr(self, 'exif_data', {})  # Пример EXIF данных
        }
    
    def process(self, operation: str, **kwargs):
        if operation == 'resize':
            new_resolution = kwargs.get('resolution', '1920x1080')
            print(f"Resizing photo {self.name} to {new_resolution}")
        elif operation == 'apply_filter':
            filter_name = kwargs.get('filter', 'grayscale')
            print(f"Applying {filter_name} filter to {self.name}")
        elif operation == 'extract_exif':
            print(f"Extracting EXIF data from {self.name}")
        else:
            print(f"Unknown operation '{operation}' for photo file")