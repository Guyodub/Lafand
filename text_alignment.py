import re

sw_file = open("./data/raw/swahili.sw","r", encoding = "utf-8").read()
en_file = open("./data/raw/english.en","r", encoding = "utf-8").read()

def text_preprocessing(lang_file, file_name):
    # split at newline character
    text = lang_file.split('\n')
    # split at full stops, for sentence alignment
    new_text = []
    for line in text: 
        new_text.append(line.split('.'))
    # flatten the nested sublists that result from the previous step
    flat_text = [item for sublist in new_text for item in sublist]
    flat_text = list(filter(None, flat_text))

    new_text2 = []
    
    for line in flat_text:
        new_text2.append(re.sub(r'[^\w\s]','',line.lower()))
    # remove any empty sensences in the list
    new_text2 = list(filter(None, new_text2))
    f = open("data/aligned/" + file_name, "w", encoding="utf-8")
    for line in new_text2: 
        # strip sentences of space either at the beginning or end
        f.write(line.lstrip())
        f.write("\n")
    f.close()

text_preprocessing(sw_file,"swahili.sw")
text_preprocessing(en_file,"english.en")

