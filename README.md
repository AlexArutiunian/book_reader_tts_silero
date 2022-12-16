# Book reader

In this reposytory is program 'book_reader.py' - it is text to speech with [silero models](https://github.com/snakers4/silero-models).

In my opinion the best voice in russian is 'xenia'. So in my project I use it. 

## Necessary library

```bash
pip3 install silero
pip3 install torch
pip3 install torchaudio
pip3 install tqdm
pip3 install sounddevice
```
If that is not enough, you can see [my list of library](https://github.com/AlexArutiunian/book_reader/blob/main/src/headers.txt) and check your list with command
```bash
pip3 list
```
## Correction of speech errors of the model

In directory [book_reader/src/helpers](https://github.com/AlexArutiunian/book_reader/tree/main/src/helpers) you can find files 'word.txt' and 'word+/txt', with which you can place accents in words of your text.
Also you can correct of another speech errors of the model with the [guide](https://github.com/snakers4/silero-models/wiki/SSML) from developers of silero model.