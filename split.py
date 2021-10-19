from sklearn.utils import shuffle

sw_file = open("./data/new_aligned/swahili.sw","r", encoding = "utf-8").read()
en_file = open("./data/new_aligned/english.en","r", encoding = "utf-8").read()

sw = sw_file.split('\n')
en = en_file.split('\n')
X,y = shuffle(en, sw, random_state=42)
train_sw = y[:1862]
test_sw = y[1863:3725]
train_en = X[:1862]
test_en = X[1863:3725]

def write_files(file_name,flat_text):
    f = open("data/new_aligned/split/" + file_name, "w", encoding="utf-8")
    for line in flat_text: 
        # strip sentences of space either at the beginning or end
        if len(line.split()) > 0:
            f.write(line.lstrip())
            f.write("\n")
    f.close()
write_files('test.en',train_en)
write_files('test.sw',train_sw)
write_files('dev.en',test_en)
write_files('dev.sw',test_sw)