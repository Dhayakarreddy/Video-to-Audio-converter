from gtts import gTTS
from playsound import stubplaysound
audio="sppech.mp3"
language='en'
sp=gTTS(test="welcome to my world",lang=language,slow=False)
sp.save(audio)
playsound(audio)
print("======audio is playing=====")