#file: my_music.py

class My_music():
    def __init__(self):
        self.music_dict = {}

    def add_track(self, track, artist):
        #track to be value, artist to be key
        self.music_dict.update({artist:track})

    def list_music(self):
        track_list = []
        artist_list = []
        counter = 1

        for value in self.music_dict.values():
            track_list.append(value)
        for key in self.music_dict.keys():
            artist_list.append(key)
        #return as a string formatted "1. Track by Artist"
        formatting = ""
        for entry in range(len(track_list)):
            formatting += f"{counter}. {track_list[entry]} by {artist_list[entry]}\n"
            counter += 1
        #Tracks nuber of entries within self.music_dict
        return formatting