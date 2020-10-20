FILE_NAME = ""  # file name goes here
SPLITER = ""  # line that split sections e.g: empty line is ""  

with open(FILE_NAME)  as f:
    file = [line.strip() for line in f]

    # list of index indicate lines that has spliter
    index = [i for i, d in enumerate(file) if d == SPLITER]  

    
