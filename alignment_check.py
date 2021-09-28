import re

sw_file = open("./data/aligned/swahili.sw","r", encoding = "utf-8").read()
en_file = open("./data/aligned/english.en","r", encoding = "utf-8").read()

def alignment_check(en_file, sw_file):
    en_file = en_file.split('\n')
    sw_file = sw_file.split('\n')
    
    if(len(en_file) == len(sw_file)):
        print("Files are aligned!!")
    else:
        print(str(abs(len(en_file) - len(sw_file))) + " line(s) mismatch")
        print("Below is a line with mismatch")

        check_discrepancy(en_file,sw_file)

def check_discrepancy(en_file, sw_file):
    
    line = []
    length = len(sw_file)
    print(length)
    for i in range(0,length):
        #print(en_file[i])
        print(en_file[i])
        print(i)
        if (en_file[i][0].isdigit()):  
            if (not sw_file[i][0].isdigit()):
                print(i)
                break
            else:
                if (re.search("^\d+\s", en_file[i]).group(0) != re.search("^\d+\s", sw_file[i]).group(0)):
                    print(i)
                    break

alignment_check(en_file,sw_file)