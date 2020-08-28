#importing the module 
from pytube import YouTube
#where to save 
link = input("YouTube Video Link")
YouTube(link).streams.first().download('C:\\Users\\Aditya\\Downloads')
print("Please Check your Downloads Folder") 