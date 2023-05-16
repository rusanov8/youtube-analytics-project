import json
from googleapiclient.discovery import build

class Channel:
    """Класс для ютуб-канала"""

    # Создаем переменную с ключом
    api_key: str = 'AIzaSyClKcu7w5bGUAq45OwsdpdXes7q7vLtLvQ'

    # Создаем объект для работы с API
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        channel_info = self.youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        print(json.dumps(channel_info, indent=1))

