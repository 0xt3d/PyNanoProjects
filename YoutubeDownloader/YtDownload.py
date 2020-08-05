from pytube import YouTube, Playlist


yt = YouTube('https://www.youtube.com/watch?v=ekYbYywaFYo')
stream = yt.streams.first()
stream.download('C://users//aditya//downloads')
