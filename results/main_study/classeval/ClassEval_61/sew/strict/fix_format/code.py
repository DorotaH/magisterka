class MusicPlayer:
    def __init__(self):
        self.playlist = list()
        self.current_song = None
        self.volume = 50

    def add_song(self, song):
        self.playlist.append(song)

    def remove_song(self, song):
        if song in self.playlist:
            self.playlist.remove(song)
            if song == self.current_song:
                self.stop()

    def play(self):
        if self.playlist and self.current_song:
            return self.playlist[0]
        elif len(self.playlist):
            return False

    def stop(self):
        if not self.current_song:
            return False
        else:
            self.current_song = None
            return True

    def switch_song(self):
        if not self.current_song:
            return False
        else:
            current_index = self.playlist.index(self.current_song)
            if current_index < len(self.playlist) - 1:
                self.current_song = self.playlist[current_index + 1]
                return True
            else:
                return False

    def previous_song(self):
        if not self.current_song:
            return False
        else:
            current_index = self.playlist.index(self.current_song)
            if current_index > 0:
                self.current_song = self.playlist[current_index - 1]
                return True
            else:
                return False

    def set_volume(self, volume):
        if not 0 <= volume <= 100:
            return False
        else:
            self.volume = volume

    def shuffle(self):
        if not self.playlist:
            return False
        else:
            import random

            random.shuffle(self.playlist)
            return True
