from pytube import YouTube, Playlist


yt = YouTube('https://www.youtube.com/watch?v=Nxs_mpWt2BA')
stream = yt.streams.first()
stream.download('C://users//aditya//downloads')
