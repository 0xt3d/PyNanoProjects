# Python code to convert video to audio 
import moviepy.editor as mp 
des = input("Enter the file path")
# Insert Local Video File Path 
clip = mp.VideoFileClip(r,des) 
rename = input("Enther the file name :")
# Insert Local Audio File Path 
clip.audio.write_audiofile(r,rename) 
