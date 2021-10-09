import re
from nltk.tokenize import sent_tokenize


sw_file = open("./data/raw/swahili.sw","r", encoding = "utf-8").read()
en_file = open("./data/raw/english.en","r", encoding = "utf-8").read()

def text_tokenization(lang_file, file_name):
    #split by new line
    text = lang_file.split('\n')

    new_text = []
    #
    for line in text:
        
        line = re.sub(r'[^\x00-\x7F\x80-\xFF\u0100-\u017F\u0180-\u024F\u1E00-\u1EFF]', u'', line)
        new_text.append(sent_tokenize(line))
    flat_text = [item for sublist in new_text for item in sublist]
    flat_text = list(filter(None, flat_text))

    f = open("data/new_aligned/" + file_name, "w", encoding="utf-8")
    for line in flat_text: 
        # strip sentences of space either at the beginning or end
        f.write(line.lstrip())
        f.write("\n")
    f.close()
    
text_tokenization(en_file,"english.en")
text_tokenization(sw_file,"swahili.sw")