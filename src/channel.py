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
        self.__channel_id = channel_id
        self.channel_info = self.youtube.channels().list(id=self.__channel_id, part='snippet,statistics').execute()
        self.title = self.channel_info['items'][0]['snippet']['title']
        self.description = self.channel_info['items'][0]['snippet']['description']
        self.url = self.channel_info['items'][0]['snippet']['customUrl']
        self.subscribers_count = self.channel_info['items'][0]['statistics']['subscriberCount']
        self.video_count = self.channel_info['items'][0]['statistics']['videoCount']
        self.total_views = self.channel_info['items'][0]['statistics']['viewCount']


    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        print(json.dumps(self.channel_info, indent=1))

    @property
    def channel_id(self) -> str:
        """Возвращает id канала."""
        return self.__channel_id


    @classmethod
    def get_service(cls):
        """Возвращает объект для работы с API вне класса"""
        return cls.youtube

    def to_json(self, json_file):
        """Сохраняет значения атрибутов в файл"""
        with open(json_file, 'w') as file:
            #`добавляю все атрибуты по отдельности кроме channel_info
            data = {}
            data['channel_id'] = self.__channel_id
            data['title'] = self.title
            data['description'] = self.description
            data['url'] = self.url
            data['subscribers_count'] = self.subscribers_count
            data['video_count'] = self.video_count
            data['total_views'] = self.total_views
            json.dump(data, file, indent=1)











