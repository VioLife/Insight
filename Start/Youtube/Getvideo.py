from tkinter import *
from pytube import YouTube
from tube_dl import YouTube, extras


root = Tk()
root.geometry("700x300")
root.resizable(0, 0)
root.title("YouTube Video Downloader")

Label(root, text="YouTube Downloader",
      font="arial 26 bold").pack()


link = StringVar()

Label(root, text="Enter video link:", font="arial 15 bold").place(x=270, y=60)
Entry(root, width=80, textvariable=link).place(x=130, y=90)


#Функция для скачивания видео из Ютуба
def Downloader():
    url = YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    Label(root, text="Success!Video is here!", font="arial 15").place(x=270, y=210)



Button(root, text="Скачать видео", font="arial 15 bold", bg="white", padx=2, command=Downloader).place(x=280, y=150)

root.mainloop()

#Функция для скачивания аудио-файла из Ютуба
def getAudio(a_url, path1):
    yt = YouTube(a_url)
    yt = yt.formats.filter_by(only_audio=True)[0]
    b = yt.download(path1) 
    b = extras.Convert(b,'mp3',add_meta=True) 


a_url = input('Input url:\n') #https://www.youtube.com/watch?v=DAtJNeTMlJg
path1 = input('Path to store file:\n')

getAudio(a_url,path1)


#YouTube('https://www.youtube.com/watch?v=hdlJZvaTI0c')
#/Users/mac/Desktop