import os
from googleapiclient.discovery import build

class Video:

    api_key: str = os.getenv('YT_API_KEY')

    # Создаем объект для работы с API
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, video_id):
        try:
            self.__video_id = video_id

            self.video_response = self.youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                                    id=self.video_id
                                                    ).execute()

            self.title = self.video_response['items'][0]['snippet']['title']
            self.url = 'https://youtu.be/' + self.__video_id
            self.views_count = self.video_response['items'][0]['statistics']['viewCount']
            self.likes_count = self.video_response['items'][0]['statistics']['likeCount']

        except Exception:
            self.title = None
            self.likes_count = None
            self.url = None
            self.views_count= None


    @property
    def video_id(self):
        return self.__video_id

    def __str__(self):
        return f'{self.title}'


class PLVideo(Video):
    def __init__(self, video_id, playlist_id):
        super().__init__(video_id)
        self.playlist_id = playlist_id

