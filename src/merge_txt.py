filenames = []
i_max = 5
i = j = 1
input = 'gen_audio/text'
while i != i_max + 1:
    j = 1
    while j != 4:
        filenames.append(f'{input}/text{i}_{j}.txt')            
        j += 1
    i += 1

output = "merge_20ch.txt"
with open(output, 'w', encoding="utf-8") as outfile:
    for fname in filenames:
        print(fname)
        with open(fname, encoding="utf-8") as infile:
            outfile.write('\n') 
            for line in infile:
                outfile.write(line) 
                                 