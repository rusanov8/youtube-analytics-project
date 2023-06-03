import os
from datetime import timedelta

import isodate as isodate
from googleapiclient.discovery import build


class PlayList:

    # Переменная с ключом API
    api_key: str = os.getenv('YT_API_KEY')

    # Объект для работы с youtube
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, playlist_id):
        self.playlist_id = playlist_id

        # Объект для получения названия плейлиста
        self.playlist = self.youtube.playlists().list(id=playlist_id,
                                             part='contentDetails,snippet',
                                             maxResults=50,
                                             ).execute()

        self.title = self.playlist['items'][0]['snippet']['title']
        self.url = "https://www.youtube.com/playlist?list=" + self.playlist_id

        # Объект для получения информации по видео в плейлисте
        self.playlist_videos = self.youtube.playlistItems().list(playlistId=playlist_id,
                                                       part='contentDetails',
                                                       maxResults=50,
                                                       ).execute()
        # Список из id всех видео плейлиста
        self.video_ids: list[str] = [video['contentDetails']['videoId'] for video in self.playlist_videos['items']]

        # Объект для работы с видео
        self.video_response = self.youtube.videos().list(part='contentDetails,statistics',
                                       id=','.join(self.video_ids)
                                       ).execute()

    @property
    def total_duration(self):
        """Возвращает суммарную длительность плейлиста"""
        total_duration = timedelta(seconds=0)
        for video in self.video_response['items']:
            duration = isodate.parse_duration(video['contentDetails']['duration'])
            total_duration += duration

        return total_duration


    def show_best_video(self):
        """Возвращает ссылку на самое популярное видео"""
        max_likes = 0
        best_video = ''
        for video in self.video_response['items']:
            if int(video['statistics']['likeCount']) > max_likes:
                max_likes = int(video['statistics']['likeCount'])
                best_video = 'https://youtu.be/' + video['id']

        return best_video
