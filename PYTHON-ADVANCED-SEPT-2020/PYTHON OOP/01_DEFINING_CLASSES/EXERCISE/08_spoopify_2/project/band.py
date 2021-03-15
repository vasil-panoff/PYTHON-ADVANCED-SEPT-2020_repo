class Band:
    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album):
        if album in self.albums:
            return f"Band {self.name} already has {album.name} in their library."
        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name):
        albums = [a for a in self.albums if a.name == album_name]
        if not albums:
            return f"Album {album_name} is not found."
        searched_album = albums[0]
        if searched_album.published:
            return "Album has been published. It cannot be removed."
        self.albums.remove(searched_album)
        return f"Album {album_name} has been removed."

    def details(self):
        result = f'Band {self.name}\n'
        for a in self.albums:
            result += a.details()
        return result