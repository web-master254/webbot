import os
import pyttsx3
from gtts import gTTS


class Speaker:
    def __init__(self):
        self.audio_folder = "audios"
        self.folder_list = os.listdir('.')
        if self.audio_folder not in self.folder_list:
            os.mkdir(self.audio_folder)
        else:
            pass
    # list_f is a function that returns the list of text files
    #args is actually a path i.e audio_folder
    def file_list(self):
        return os.listdir(self.audio_folder)

    def speak(self,content,audio_file=None):
        x = content(self.audio_folder)
        if audio_file == None:
            audio_file = os.path.join(self.audio_folder,os.path.splitext(x)[0],'.mp3')
        if os.path.isfile(x):
            if content.endswith('.txt'):
                 with open(x) as fil:
                    audio = gTTS(fil.read())
                    audio.save(audio_file)
            else:
                raise Exception("Can't read this type of file.")
        else:
            #raise Exception("You gave no file. Maybe it is a folder. Check again")
            pass
        

    def list_all(self,folder):
        for i in folder:
            return i
        

x = Speaker()
x.speak(x.list_all)

        
        
       