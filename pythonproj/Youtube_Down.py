from pytube import YouTube
from tkinter import filedialog
from tkinter import ttk
from tkinter import *
import re
import threading
from tkinter.font import Font


class Application:


    def __init__(self,root):
        self.root=root
        self.root.grid_rowconfigure(0,weight=2)
        self.root.grid_columnconfigure(0,weight=1)
        self.root.config(bg="#ffdddd")
        top_label=Label(self.root,text="YouTube Download Manager",fg='orange',font=("Helvetica",70))
        top_label.grid(pady=(0,10))
        link_label=Label(self.root,text="Please Place any YouTube Video Link Below",font=('Snowpersons',30))
        link_label.grid(pady=(0,20))

        self.youtubeEntryVar=StringVar()
        self.youtubeEntry=Entry(self.root,width=70,textvariable=self.youtubeEntryVar,font=('Agency Fb',25),fg="red")
        self.youtubeEntry.grid(pady=(0,15),ipady=4)

        self.youtubeEntryError=Label(self.root,text="",font=('Concert One',20))
        self.youtubeEntryError.grid(pady=(0,8))

        self.youtubeFileSave=Label(self.root,text="Choose Directory",font=('Concert One',30))
        self.youtubeFileSave.grid()
        self.youtubeFileDirectoryButton=Button(self.root,text="Directory",font=('Bell MT',15),command=self.openDirectory)
        self.youtubeFileDirectoryButton.grid(pady=(10,3))

        self.fileLocationLabel=Label(self.root,text="",font=('Freestyle Script',25))
        self.fileLocationLabel.grid()
        self.youtubeChooseLabel=Label(self.root,text="Choose the Download Type",font=('Variety',30))
        self.youtubeChooseLabel.grid()
        self.downloadChoice=[("Audio MP3",1),("Video MP4",2)]
        self.ChoiceVar=StringVar()
        self.ChoiceVar.set(1)
        for text,mode in self.downloadChoice:
            self.youtubeChoices=Radiobutton(self.root,text=text,font=("Northwest old",15),variable=self.ChoiceVar,value=mode)
            self.youtubeChoices.grid()
        
        self.downloadButton=Button(self.root,text="Download",width=10,font=("Bell MT",15),command=self.checkyoutubelink)
        self.downloadButton.grid(pady=(30,5))

        
    def openDirectory(self):
        self.foldername=filedialog.askdirectory()
        if(len(self.foldername)>0):
            self.fileLocationLabel.config(text=self.foldername,fg="green")
            return True
        else:
            self.fileLocationLabel.config(text="Please Choose a Directory",fg="red")

    
    def checkyoutubelink(self):
        self.matchyoutubelink=re.match("^https://www.youtube.com/.",self.youtubeEntryVar.get())
        if(not self.matchyoutubelink):
            self.youtubeEntryError.config(text="Invalid Youtube link",fg='red')
        elif(not self.openDirectory):
            self.fileLocationLabel(text="Please Choose a Directory",fg='red')
        elif(self.matchyoutubelink and self.openDirectory):
            self.downloadWindow()

    def downloadWindow(self):
        self.newWindow=Toplevel(self.root)
        self.root.withdraw()
        self.newWindow.state("zoomed")
        self.newWindow.grid_rowconfigure(0,weight=0)
        self.newWindow.grid_columnconfigure(0,weight=1)
        self.app=SecondApp(self.newWindow,self.youtubeEntryVar.get(),self.foldername,self.ChoiceVar.get())

class SecondApp:
    def __init__(self,downloadWindow,youtubelink,Foldername,Choices):
        self.downloadWindow=downloadWindow
        self.youtubelink=youtubelink
        self.Foldername=Foldername
        self.Choices=Choices

        self.yt=YouTube(self.youtubelink)

        if(Choices=='1'):
            self.video_type=self.yt.streams.filter(only_audio=True)
            self.MaxFileSize=self.video_type.filesize
        if(Choices=='2'):
            self.video_type=self.yt.streams.first()
            self.MaxFileSize=self.video_type.filesize

        self.loadingLabel=Label(self.downloadWindow,text="Downloading In Progress......",font=("Small Fonts",40))
        self.loadingLabel.grid(pady=(100,0))
        self.loadingPercent=Label(self.downloadWindow,text="0",fg="green",font=("Agency Fb",40))
        self.loadingPercent.grid(pady=(50,0))
        self.progress_bar=ttk.Progressbar(self.downloadWindow,length=500,orient='horizontal',mode='indeterminate')
        self.progress_bar.grid(pady=(50,0))
        self.progress_bar.start()
        threading.Thread(target=self.yt.register_on_progress_callback(self.show_progress)).start()
        threading.Thread(target=self.downloadFile).start()
    def downloadFile(self):
        if(self.Choices=='1'):
            self.yt.streams.filter(only_audio=True).first().download(self.Foldername)
        if(self.Choices=='2'):
            self.yt.streams.first().download(self.Foldername)
    def show_progress(self,streams=None,Chunks=None,filehandle=None,bytes_remaining=None):
        self.percent_count=float("%0.2f" (100-(100*(bytes_remaining/self.MaxFileSize))))
        if(self.percent_count<100):
            self.loadingPercent.config(text=self.percent_count)
        else:
            self.progress_bar.stop()
            self.loadingLabel.grid_forget()
            self.progress_bar.grid_forget()

            self.downloadFinished=Label(self.downloadWindow,text="Download Finished",font=("Agency Fb",30))
            self.downloadFinished.grid(pady=(150,0))
            
            self.downloadFileName=Label(self.downloadWindow,text=self.yt.title,font=("Terminal",30))
            self.downloadFileName.grid(pady=(50,0))

            MB=float("%0.2f"% (self.MaxFileSize/1000000))
            self.downloadFileSize=Label(self.downloadWindow,text=str(MB),font=("Agency Fb",30))
            self.downloadFileSize.grid(pady=(50,0))
    
        

if __name__=="__main__":
    window=Tk()
    window.title("Youtube Download Manager")
    window.state("zoomed")
    app=Application(window)
    


    mainloop()