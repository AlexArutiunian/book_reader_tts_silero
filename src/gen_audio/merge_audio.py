from pydub import AudioSegment
import os

path_ = r"src/gen_audio/sounds"
path_ = os.path.abspath(path_)
lst = [rf"{path_}/1_2.wav"]
i = 2
while(i != 2):
    j = 1
    while(j != 3):
        name = f"{path_}/{i}_{j}.wav"
        lst.append(name)
        j += 1
    i += 1  
   

for audio in lst:
    print(audio)

merge_ = AudioSegment.from_file(f"{path_}/1_1.wav", format="wav")
for audio in lst:
    print(audio)
    sound = AudioSegment.from_file(audio, format="wav")
    merge_ += sound   

merge_.export(f"{path_}/merge.mp3", format="mp3")
