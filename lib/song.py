class Song:
    count=0
    genres=[]
    artists=[]
    genre_count={}
    artist_count={}
    def __init__(self,name,artist,genre):
        self.name=name
        self.artist=artist
        self.genre=genre
        Song.add_song_to_count()
        Song.add_to_genres(self.genre)
        Song.add_to_artists(self.artist)
        Song.add_to_genre_count(self.genre)
        Song.add_to_artist_count(self.artist)


    
    @classmethod
    def add_song_to_count(self):
        Song.count+=1
        
    @classmethod
    def add_to_genres(cls,value):
        if not value in Song.genres:
         Song.genres.append(value)
    
    @classmethod
    def add_to_artists(cls,value):
        if not value in Song.artists:
         Song.artists.append(value)
    @classmethod
    def add_to_genre_count(cls,value):
        if value not in cls.genre_count:
            cls.genre_count[value]=1
        else:
            cls.genre_count[value]+=1
   
    @classmethod
    def add_to_artist_count(cls,value):
        if value not in cls.artist_count:
            cls.artist_count[value]=1
        else:
            cls.artist_count[value]+=1


      
out_of_touch = Song("Out of Touch", "Hall and Oates", "Pop")
ninety_nine_problems = Song("99 Problems", "Jay-Z", "Rap")
out_of_t8ouch = Song("Out of Touch", "Hall and Oates", "Pop")


# print(Song.count)
# print(Song.genres)
# print(Song.artists)
print(Song.genre_count)
print(Song.artist_count)