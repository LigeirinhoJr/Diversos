from pytube import YouTube

link = input("Enter Url: ")

video = YouTube(link)

stream = video.streams.get_highest_resolution()

stream.download()