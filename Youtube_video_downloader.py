import tkinter
import customtkinter
from pytube import YouTube

APP_HEIGHT = 300
APP_WIDTH = 500


def on_progress(stream, chunk, bytes_remaining):
    # Calculate the download percentage
    progress = round((1 - bytes_remaining / stream.filesize) * 100, 2)
    print(f"Downlowding... {progress}%")
    progress_var.set(progress / 100)
    progress_val.set("Downlowding ... {} % ".format(round(progress, 2)))
    app.update()


def download():
    try:

        url = link.get()
        print(url)

        yt = YouTube(url, on_progress_callback=on_progress)
        progress_bar = customtkinter.CTkProgressBar(app, variable=progress_var, width=200, height=10,
                                                    progress_color="#008800", mode="determinate" , border_width=2 , border_color="#888888" )
        progress_bar.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)

        progress_downval= tkinter.Label(app , textvariable=progress_val , font=("Helvetica 15 normal ") ,  background="#FFFFFF" )
        progress_downval.place(relx =  0.5 , rely = 0.8 , anchor=tkinter.CENTER)

        video = yt.streams.get_highest_resolution()
        video.download(".")
        finishlabel = customtkinter.CTkLabel(app, text="The Video is downloaded successfully !",
                                             font=customtkinter.CTkFont(family='<Helvetica>', size=12),
                                             text_color="#00FF00")
        finishlabel.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)
        titleLabel = customtkinter.CTkLabel(app, text=f"{yt.title}",
                                            font=customtkinter.CTkFont(family='<Helvetica>', size=12))
        print(f"Downloading: {yt.title}")
        titleLabel.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)
        finishlabel.after(10000, finishlabel.destroy)
        titleLabel.after(10000, titleLabel.destroy)
        progress_bar.destroy()
        progress_downval.destroy()

    except Exception as e:
        print(f"Error : {str(e)} ")
        error = str(e)
        finishlabel = customtkinter.CTkLabel(app, text="Error ! {}".format(error),
                                             font=customtkinter.CTkFont(family='<Helvetica>', size=12),
                                             fg_color="#FF0000")
        finishlabel.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)
        finishlabel.after(5000, finishlabel.destroy)

    app.update()


customtkinter.set_appearance_mode("System")
app = customtkinter.CTk()
app.geometry(f"{APP_WIDTH}x{APP_HEIGHT}")
app.resizable(False, False)
app.title("Youtube Video Downloader")

label = customtkinter.CTkLabel(app, text="Put the link of the video :",
                               font=customtkinter.CTkFont(family='<Helvetica>', size=12))
label.pack()

progress_var = customtkinter.DoubleVar()
progress_val = tkinter.StringVar()

Video_link = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=380, height=30, textvariable=Video_link)
link.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER)

button_download = customtkinter.CTkButton(app, text="Download", command=download, fg_color="#00AA00",
                                          hover_color="#007700")
button_download.place(relx=0.5, rely=0.45, anchor=tkinter.CENTER)

app.mainloop()
