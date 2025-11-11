from models.audio import AudioFile
from models.video import VideoFile
from models.photo import PhotoFile
from storage.local import LocalStorage
from storage.cloud import CloudStorage

def demonstrate_media_operations():
    """Демонстрация работы с медиа-файлами"""
    
    # Создание медиа-файлов разных типов
    audio = AudioFile("song.mp3", 1024000, "user1", 180.5, 320, 44100)
    video = VideoFile("movie.mp4", 50000000, "user2", 3600.0, "1920x1080", 30.0)
    photo = PhotoFile("photo.jpg", 2500000, "user3", "4000x3000", "Canon EOS R5")
    
    # Вывод метаданных
    print("=== Метаданные файлов ===")
    print("Audio metadata:", audio.get_all_metadata())
    print("Video metadata:", video.get_all_metadata())
    print("Photo metadata:", photo.get_all_metadata())
    
    # Операции с файлами
    print("\n=== Операции с файлами ===")
    audio.process('convert', format='wav')
    video.process('extract_frame', timestamp=120)
    photo.process('resize', resolution='1024x768')
    
    # Работа с разными хранилищами
    print("\n=== Работа с хранилищами ===")
    
    # Локальное хранилище
    local_storage = LocalStorage("./media_files")
    # local_storage.save(open('song.mp3', 'rb'), 'audio/song.mp3')
    
    # Облачное хранилище
    cloud_storage = CloudStorage(
        bucket_name="my-media-bucket",
        endpoint="s3.cloudprovider.com",
        access_key="access_key",
        secret_key="secret_key"
    )
    # cloud_storage.save(open('movie.mp4', 'rb'), 'video/movie.mp4')
    
    print("Демонстрация завершена!")

def demonstrate_extensibility():
    """Демонстрация легкости добавления новых типов"""
    
    # Предположим, мы хотим добавить новый тип - DocumentFile
    class DocumentFile:
        # Нам нужно будет создать новый класс, унаследованный от MediaFile
        # и реализовать абстрактные методы
        pass
    
    # Или новое хранилище - FTPStorage
    class FTPStorage:
        # Наследуемся от Storage и реализуем абстрактные методы
        pass
    
    print("Система легко расширяется новыми типами файлов и хранилищ!")

if __name__ == "__main__":
    demonstrate_media_operations()
    demonstrate_extensibility()