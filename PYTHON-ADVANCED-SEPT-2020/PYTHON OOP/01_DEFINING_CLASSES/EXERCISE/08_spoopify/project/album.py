from typing import List
from project.song import Song:


class Album:
    name: str
    songs: List[Song]
    published: bool

    def __init__(self, name, *songs):
        self.name = name
        self.songs = list(songs)
