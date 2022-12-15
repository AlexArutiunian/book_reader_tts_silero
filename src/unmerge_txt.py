
i_max = 6
def unmerge_(outfile):
    out = open(outfile, 'w', encoding="utf-8")    
    for line in file:
        if (line == "</speak>") + (line == "\n</speak>\n") + (line == "</speak>\n") + (line == "\n</speak>"):
            out.write(line)
            print(line) 
            print(outfile)
            break
        else:
            out.write(line) 

filename = 'merge_20ch.txt'
file = open(filename, 'r', encoding="utf-8")
i = 1
while i != i_max + 1:
    j = 1
    while j != 4:
        outfile = f'gen_audio/text/text{i}_{j}.txt'
        unmerge_(outfile)                  
        j += 1
    i += 1                
     