#Import packages
import speech_recognition as sr 
import moviepy.editor as mp
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

#70 minutes converted in seconds
num_seconds_video= 70*60 + 2
print("The video is {} seconds".format(num_seconds_video))
l=list(range(0,num_seconds_video+1,60))
print(l)

#here you create chunks of audio to be transcribed into text
diz={}
for i in range(len(l)-1):
    ffmpeg_extract_subclip("YOUR MP4 FILE HERE", l[i]-2*(l[i]!=0), l[i+1], targetname="cut{}.mp4".format(i+1))
    clip = mp.VideoFileClip("cut{}.mp4".format(i+1)) 
    clip.audio.write_audiofile("converted{}.wav".format(i+1))
    r = sr.Recognizer()
    audio = sr.AudioFile("converted{}.wav".format(i+1))
    with audio as source:
      r.adjust_for_ambient_noise(source)  
      audio_file = r.record(source)
    print(type(audio_file))
    result = r.recognize_google(audio_file,"es-ES")
    diz['chunk{}'.format(i+1)]=result

l_chunks=[diz['chunk{}'.format(i+1)] for i in range(len(diz))]
text='\n'.join(l_chunks)

#here we do the actual transcription
with open('recognized.txt',mode ='w') as file: 
   file.write("Recognized Speech:") 
   file.write("\n") 
   file.write(text) 
   print("Finally ready!")