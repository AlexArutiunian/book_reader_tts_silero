import re
import codecs
import itertools
import os
import shutil
import torch
import pathlib
from tqdm import tqdm
from pydub import AudioSegment

def delete_bad_sym(fname):
    with open(fname, "r", encoding="utf-8") as f:
        content = f.read()
        c = re.sub("[\'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz]", "", content)
    with open(fname, "w", encoding="utf-8") as f:
        f.write(c)    

def lower_sym(fname):
    lst1 = []
    lst2 = [] 
    dump_strfile_in_lst('src\\helpers\\alpA.txt', lst1)
    dump_strfile_in_lst('src\\helpers\\alp.txt', lst2)         
    for elem1, elem2 in zip(lst1, lst2):        
        replace_word(fname, f"{elem1}", f"{elem2}")                

def add_plus_and_textnum(fname):
    lst1 = []
    lst2 = []
    dump_strfile_in_lst('src\\helpers\\word.txt', lst1)
    dump_strfile_in_lst('src\\helpers\\word+.txt', lst2)               
    for elem1, elem2 in zip(lst1, lst2):
        replace_word(fname, f" {elem1} ", f" {elem2} ") 

def dump_strfile_in_lst(filename, lst):
    filename = os.path.abspath(filename)
    with open(f'{filename}', 'r', encoding="utf-8") as file:
        for line in file:
            lst.append(line.rstrip()) 


def replace_word(fname, before, after):
    with open(fname, 'r', encoding="utf-8") as file :
        filedata = file.read()        
    filedata = filedata.replace(before, after)  
    with open(fname, 'w', encoding="utf-8") as file:
        file.write(filedata) 

def parts_(sourcefile, path_outfiles, i_max, j_max):
    f = open(f"{sourcefile}", "r", encoding="utf-8") 
    for i in range(i_max):
        for j in range(j_max):
            res = open(rf'{path_outfiles}\\text{i + 1}_{j + 1}.txt', "w", encoding="utf-8")
            res.write("\n<speak>\n")
            c = '\n'
            for k in range(850):
                c = f.read(1)    
                if((k > 800) * (c == '.')):
                    res.write(c)
                    break
                else:
                    res.write(c)
                    if((c == '.') + (c == ' ') * (k % 50 == 0)):
                        res.write('\n')

            c = f.read(1)
            if(c != ' '):
                res.write(c)
                t = 0
                while(t != 100):
                    c = f.read(1)
                    if(c == ' '):
                        break
                    res.write(c)
                    t += 1
                           
            res.write("\n</speak>\n")                     

def TTS(name_file, model):
    with open(name_file, "r", encoding="utf-8") as file:
            ssml_sample = file.read()
            sample_rate = 48000
            speaker='xenia'
            print(ssml_sample)
            audio_paths = model.save_wav(ssml_text=ssml_sample,
                                        speaker=speaker,
                                        sample_rate=sample_rate, 
                                        audio_path=path)
def text_prepare(fname, outfiles, i_max):
    delete_bad_sym(fname)
    lower_sym(fname)
    add_plus_and_textnum(fname)
    replace_word(fname, "страница", "<p> страница </p>")
    parts_(fname, outfiles, i_max, 3)                                        

def size_file(out_text):
    n = 0
    with open(out_text, 'r', encoding="utf-8") as f:
        while True:
            c = f.read(1)
            n += 1
            if not c:
                break
    return n        

if __name__ == "__main__":

    num_chapter = 20
    print("Input name of file for text to speech: ")
    f = " "
    f = input()
    fname = rf"input_text/{f}"
    out_text = rf"src/file_input.txt"
    outfiles = r"src/gen_audio/text"
    
   
  
    fname = os.path.abspath(fname)
    out_text = os.path.abspath(out_text)
    outfiles = os.path.abspath(outfiles)
 
    shutil.copyfile(fname, out_text)
   
    size_f = size_file(out_text)   
    print(size_f)
    i_max = (int)(size_f / 2100)
    print("imax = ", i_max)

    text_prepare(out_text, outfiles, i_max)

    device = torch.device('cpu')
    torch.set_num_threads(4)
    local_file = 'model.pt'

    if not os.path.isfile(local_file):
        torch.hub.download_url_to_file('https://models.silero.ai/models/tts/ru/v3_1_ru.pt',
                                    local_file)  

    model = torch.package.PackageImporter(local_file).load_pickle("tts_models", "model")
    model.to(device)

    i = j = 1
    while i != i_max + 1:
        j = 1
        while j != 4:
            path = rf"src\\gen_audio\\sounds\\{i}_{j}.wav"
            print(rf"sounds/{i}_{j}")
            TTS(rf'src\\gen_audio\\text\\text{i}_{j}.txt', model)
            j += 1                                
        i += 1

    path_ = "src\\gen_audio\\sounds"
    lst = [rf"{path_}\\1_2.wav", rf"{path_}\\1_3.wav"]
    i = 2
    while(i != i_max + 1):
        j = 1
        while(j != 4):
            name = rf"{path_}\\{i}_{j}.wav"
            lst.append(name)
            j += 1
        i += 1    
    for audio in lst:
        print(audio)

    merge_ = AudioSegment.from_file(rf"{path_}\\1_1.wav", format="wav")
    for audio in lst:
        print(audio)
        sound = AudioSegment.from_file(audio, format="wav")
        merge_ += sound   

    out_audio = rf"output_audio"
    out_audio = os.path.abspath(out_audio)
    merge_.export(rf"{out_audio}\\audio(from_{f}).mp3", format="mp3")