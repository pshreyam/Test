from gtts import gTTS
import os

class TextToAudio():
    def to_audio(self,text):
        speech = gTTS(text=text, lang='en')
        speech.save("msg.mp3")
        self.open_audio()
    def open_audio(self):   
        os.system("msg.mp3")

class FileToAudio():
    def to_audio(self,file):
        fileobj=open(file,'r')
        text=fileobj.read().strip()
        fileobj.close()
        speech = gTTS(text=text, lang='en')
        speech.save("msg.mp3")
        self.open_audio()
    def open_audio(self):   
        os.system("msg.mp3")

'''
text=input("Enter a message: ")
tta=TextToAudio()
tta.to_audio(text)
#tta.open_audio()
'''

fta=FileToAudio()
fta.to_audio("text.txt")