import os
print("Input name of file for text to speech: ")
f = " "
f = input()
fname = rf"input_text/{f}"
out_text = rf"src/file_input.txt"
outfiles = r"src/gen_audio/text"

fname = os.path.abspath(fname)
out_text = os.path.abspath(out_text)
outfiles = os.path.abspath(outfiles)

print(fname)