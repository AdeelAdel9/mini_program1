from pytube.__main__ import YouTube
from tkinter import filedialog
from pytube.streams import Stream

url_input = input("Enter your URL: ")
all_streams = YouTube(url_input).streams.all()
v=-1
for  i in all_streams:
    v=v+1
    print(str(v)+ " : "+str(i))
    stm_input = int(input("Please choose the stream: "))
    print("Please choose directroy to save: ")
    folder_name = filedialog.askdirectory()
    choice = all_streams[stm_input].download(folder_name)
    print("downloaded complited.......")
    
    
