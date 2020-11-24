from tkinter import *
import sounddevice as sd
import soundfile as sf
import random


class VoiceRecorder:
    def __init__(self,root):
        self.root=root
        self.root.title("Voice Recorder")
        self.root.geometry("300x100")
        self.root.iconbitmap("logo575.ico")
        self.root.resizable(0,0)



        def on_enter1(e):
            but['background']="black"
            but['foreground']="cyan"  
        def on_leave1(e):
            but['background']="SystemButtonFace"
            but['foreground']="SystemButtonText"

        
        def record():
            fs=40000
            sound_duration=10
            myrecord=sd.rec(int(sound_duration*fs),samplerate=fs,channels=2)

            sd.wait()

            s=random.randint(1,100)

            return sf.write('myaudio{}.flac'.format(s),myrecord,fs)



#===================frame=============================#
        
        mainframe=Frame(self.root,width=300,height=100,relief="ridge",bd=3,bg="gray66")
        mainframe.place(x=0,y=0)


        but=Button(mainframe,width=19,text="Start",font=('times new roman',12),cursor="hand2",command=record)
        but.place(x=55,y=30)
        but.bind("<Enter>",on_enter1)
        but.bind("<Leave>",on_leave1)


if __name__ == "__main__":
    root=Tk()
    VoiceRecorder(root)
    root.mainloop()