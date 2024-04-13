from project.album import Album


class Band:
    def __init__(self, name: str):
        self.name = name
        self.albums = []

    def add_album(self, album: Album):
        if album not in self.albums:
            self.albums.append(album)
            return f"Band {self.name} has added their newest album {album.name}."
        return f"Band {self.name} already has {album.name} in their library."

    def remove_album(self, album_name: str):
        try:
            album = next(filter(lambda a: a.name == album_name, self.albums))
        except StopIteration:
            return f"Album {album_name} is not found."

        if album.published == True:
            return "Album has been published. It cannot be removed."

        self.albums.remove(album)
        return f"Album {album_name} has been removed."

    def details(self):
        album_details = "".join(s.details() for s in self.albums)
        return f"Band {self.name}\n{album_details}\n"
